function [firing_rate] = runModel(g)
% this function will simulate the signaling-electrophysiology model
% the ode's for the model are in the file odemodel.m
%%%% input: g, a vector of 6 values weighting the reference levels of AT1R
%%%%%%% and five channels: gNa, gKdr, gKa, gKahp, gCaL
%%%%%%% code to run reference simulation:
%%%%%%% [firing_rate] = runModel([1,1,1,1,1,1]); 
%%%% output: firing rate (firing_rate)

options = odeset( 'RelTol', 1e-9, 'AbsTol', 1e-9 );

% simulation time parameters
ti      = -1;               % initial simulation time (s)
dt      = 0.5*10^(-3);      % time step (0.0005 s)
tf      = 300;              % final simulation time (s)
tspan   = ti:dt:tf;         % simulation time span (s)

% load initial conditons
y0      = LoadInitialConditions;

% modify AT1R level according to input g(1)
% these parameters are part of the AT1R complex
y0(94)  = y0(94)*g(1);
y0(116) = y0(116)*g(1);
y0(117) = y0(117)*g(1);
y0(118) = y0(118)*g(1);
y0      = abs(y0);

% load model parameters
% input g is supplied to LoadParameters so that conductances are modified
params  = LoadParameters(g);

% AngII stimulus, applied continuously starting at t = 0
AngII100 = [ti:0.01:(tf+1); ti:0.01:(tf+1)]';
AngII100(AngII100(:,1)<0,2) = 0;
AngII100(AngII100(:,1)>0,2) = 0.1;

% run simuations
[t, y] = ode15s(@odemodel, tspan, y0, options, params, AngII100);

% determine firing rate
[tp_fr fr index]    = freq(t,y(:,179));
firing_rate         = interp1(tp_fr, fr,tspan);

%%%%% error checking %%%%%
% replace firing rate output with zeros simulation errors occur

%%% check the length of the firing rate vector
%%% if too short, replace with zeros
if (length(firing_rate) < length(tspan))
    firing_rate = zeros(length(tspan),1);
end

%%% check for nan's and replace with zeros
indNAN = find(isnan(firing_rate));
if (isempty(indNAN)>0)
    firing_rate(indNAN) = 0;
end

figure;
plot(tspan,firing_rate)
xlabel('time (s)');
ylabel('firing rate (Hz)')

end

function [tp, f, index] = freq(t,x)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Function to calculate firing frequency
%
%  inputs: t - time vector
%          x - oscillating function (indices should match t)
%
%  outputs: tp - time points 
%           f  - corresponding frequency (at that time point)
%           index - indices of the time vector
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
k=1;
index=1;
tp=t(1);

for i=1:length(t)-1
    if (x(i)<-0&x(i+1)>-0), 
        tp(k)=t(i); 
        k=k+1; 
        index = i;    
    end
end

try
    f=[1./diff(tp)];
    f=[f, f(end)];
    tp=[tp];
catch
     tp=[t(1) t(end)];
     f=[0, 0];
end

end