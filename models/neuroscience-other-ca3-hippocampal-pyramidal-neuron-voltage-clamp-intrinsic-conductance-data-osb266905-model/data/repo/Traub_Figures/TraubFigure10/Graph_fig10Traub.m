%Code takes Traub model traces and determines
%firing/burst rate. 

%magnitude of injected current
s=[0 .025 .05 .1 .15 .2 .25 .275 .3 .5 .6 .7 .8 .9 1];
%Length for s=16
n_s = length(s);

frequency=zeros(1,n_s);
for i=1:n_s
        Name=strcat('fig10soma_i',num2str(s(i)),'.txt');
        othername=strcat(num2str(s(i)),'nA');
        data=readtable(Name);
        data=table2array(data);

        n_data = length(data(:,1));
        %find positive slope crossing of 5 mV threshold
        ind_cross = find( (data(1:n_data-1,2)<5).* (data(2:n_data,2)>=5) );
        cross = data(ind_cross,1);
        TimeIntervals = diff(cross);
        
        %pick the last interval, since it will be closest to steady state
        frequency(i) = 1/TimeIntervals(end); %in kHz  
       
        frequency(i) = frequency(i)*1e3; %in Hz (i.e., spk/s)
        
        if ( 0 == 1 )
            %for debugging purposes
            figure; plot(data(:,1),data(:,2));
            hold on;
            plot(cross,ones(size(cross))*5,'xr');
            title(othername);
        end
end

%Plotting figure 10A of Traub Paper
%s(1:9) = Currents up to .3nA in Traub, i.e., Panel A
figure
plot(s(1:9),frequency(1:9),'-s','MarkerSize',20) 
title('Figure 10 Bursts in Traub Current')
ylabel('Burst Frequencey (Hz)')
xlabel('Somatic Injected Current (nA)')

%Plotting figure 10B of Traub paper
%s(10:15) = Currents over .45nA in Traub, i.e. Panel B
figure 
plot(s(10:15),frequency(10:15),'-s','MarkerSize',20)
title('Figure 10 Spikes in Traub Current')
ylabel('Spike Frequencey (Hz)')
xlabel('Somatic Injected Current (nA)')
