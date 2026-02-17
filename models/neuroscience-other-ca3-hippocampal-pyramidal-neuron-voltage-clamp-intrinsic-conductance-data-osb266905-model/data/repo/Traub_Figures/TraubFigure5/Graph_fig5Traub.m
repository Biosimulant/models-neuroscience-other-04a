% Graph_fig5Traub
%Temporal Range in Figure 5 seems to be about 15ms

%The spikes to be plotted for each simulation were hand picked, hence the
%hardcoded temporal ranges in the plotting

Soma1=readtable('fig5soma_i1.txt');
Soma2=readtable('fig5soma_i4.txt');
Soma3=readtable('fig5soma_i5.txt');
dt=0.025;	% sample time (ms)
Soma1=table2array(Soma1);
Soma2=table2array(Soma2);
Soma3=table2array(Soma3);

%Locate peaks in each trace

% will plot 8th Peak
[Pks1,locs1]=findpeaks(Soma1(:,2));


% will plot 10th Peak
[Pks2,locs2]=findpeaks(Soma2(:,2));

% will plot 10th Peak
[Pks3,locs3]=findpeaks(Soma3(:,2));


%Use interval 9 ms before and 6 ms after for plotting range
index_interval = (-9/dt):(6/dt);
time_interval = index_interval*dt;

figure
hold on

plot(time_interval,Soma1(locs1(8)+index_interval,2))
plot(time_interval,Soma2(locs2(10)+index_interval,2))
plot(time_interval,Soma3(locs3(10)+index_interval,2))

legend('Somatic Current: 0.1 nA','Somatic Current: 0.4 nA','Somatic Current: 0.5 nA')
title('Fig 5')
xlabel('Time (ms)')
ylabel('Membrane Potential (mV)')

