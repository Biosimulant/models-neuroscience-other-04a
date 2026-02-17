% Graph_fig9Traub

Fs = 40; % points per ms
figure
for i=0:2

	Name1=strcat('fig9_apical[2]panel',num2str(i),'.txt');
	Name2=strcat('fig9_apical[5]panel',num2str(i),'.txt');
	Name3=strcat('fig9_Somapanel',num2str(i),'.txt');
	TraubFig9Apical5=readtable(Name2);
	TraubFig9Apical5=table2array(TraubFig9Apical5);
	if (i==0)
		idx=3090*Fs:3250*Fs;
	elseif (i==1)
		idx=2030*Fs:2190*Fs;
	else
		idx=3190*Fs:3350*Fs;
	end

	subplot(3,3,i+1)
	plot(TraubFig9Apical5(idx,1),TraubFig9Apical5(idx,2))
	ylim([-10 100])
	title('0.3 nA somatic current step')
	ylabel('Membrane Potential (mV) Apical Dendrite 0.6 \lambda from Soma')    
	xlabel('Time (ms)')

	TraubFig4Apical3=readtable(Name1);
	TraubFig4Apical3=table2array(TraubFig4Apical3);
	subplot(3,3,i+4)
	plot(TraubFig4Apical3(idx,1),TraubFig4Apical3(idx,2))
	ylim([-10 100])
	title('0.5 nA somatic current step')
	ylabel('Membrane Potential (mV) Apical Dendrite 0.3 \lambda from Soma')
	xlabel('Time (ms)')

	TraubFig4Soma=readtable(Name3);
	TraubFig4Soma=table2array(TraubFig4Soma);
	subplot(3,3,i+7)
	plot(TraubFig4Soma(idx,1),TraubFig4Soma(idx,2))
	ylim([-10 100])
	title('1.5 nA step injected in apical dendrite 0.6 \lambda from soma')
	ylabel('Somatic Membrane Potential (mV)')
	xlabel('Time (ms)')
    
end
