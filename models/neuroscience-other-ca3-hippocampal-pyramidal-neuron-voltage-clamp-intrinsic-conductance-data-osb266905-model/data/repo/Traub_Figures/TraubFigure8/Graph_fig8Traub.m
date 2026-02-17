% Graph_fig8Traub

figure
if ~verLessThan('matlab','9.5')
	sgtitle('Figure 8')
end

for i=0:4
	Name=strcat('fig8_Somapanel',num2str(i),'.txt');
	TraubgFig8=readtable(Name);
	TraubgFig8=table2array(TraubgFig8);
	subplot(5,1,5-i)
	plot(TraubgFig8(:,1),TraubgFig8(:,2))
	title([num2str((5-i)/10),' nA'])
	xlabel('Time (ms)')
end

