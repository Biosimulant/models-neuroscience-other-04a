% Graph_fig4Traub

figure
Fs = 40;	% sample points per ms
Trange=[200,500];	% time range to plot (ms)
tx = Trange(1)*Fs:Trange(2)*Fs;	% sample points
title('Traub Figure 4')
for i=0:2
	subplot(3,1,i+1)
	Name=strcat('fig4_panel',num2str(i),'.txt');
	TraubFig4=readtable(Name);
	TraubFig4=table2array(TraubFig4);
	plot(TraubFig4(tx,1),TraubFig4(tx,2));
	set(gca,'YTick',-10:10:90);
	ylabel('Membrane Potential (mV)')
end
xlabel('Time (ms)')

