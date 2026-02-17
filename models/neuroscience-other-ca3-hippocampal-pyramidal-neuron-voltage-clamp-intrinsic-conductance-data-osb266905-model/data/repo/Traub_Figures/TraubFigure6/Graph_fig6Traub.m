% Graph_fig6Traub
figure
title('Figure 6')

for i=0:2
    Name1=strcat('fig6_apical[2]panel',num2str(i),'.txt');
    Name2=strcat('fig6_apical[5]panel',num2str(i),'.txt');
    Name3=strcat('fig6_Somapanel',num2str(i),'.txt');
    TraubFig4Apical5=readtable(Name2);
    TraubFig4Apical5=table2array(TraubFig4Apical5);
    
    subplot(3,3,i+1)
    plot(TraubFig4Apical5(:,1),TraubFig4Apical5(:,2))
    ylim([-10 100])
    ylabel('Membrane Potential (mV) at Apical Dendrite 0.6 \lambda from soma')
    xlabel('Time (ms)')
    
    TraubFig4Apical3=readtable(Name1);
    TraubFig4Apical3=table2array(TraubFig4Apical3);
    subplot(3,3,i+4)
    plot(TraubFig4Apical3(:,1),TraubFig4Apical3(:,2))
    ylim([-10 100])
    ylabel('Membrane Potential (mV) at Apical Dendrite 0.3 \lambda from soma')
    xlabel('Time (ms)')
    
    TraubFig4Soma=readtable(Name3);
    TraubFig4Soma=table2array(TraubFig4Soma);
    subplot(3,3,i+7)
    plot(TraubFig4Soma(:,1),TraubFig4Soma(:,2))
    ylim([-10 100])
    ylabel('Somatic Membrane Potential (mV)')
    xlabel('Time (ms)')
end
