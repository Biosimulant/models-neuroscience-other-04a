% Graph_fig7Traub

ApicalCxi=readtable('TraubFig7apicalcxi_vect.txt');
ApicalCxi=table2array(ApicalCxi);
ApicalV=readtable('TraubFig7ApicalV.txt');
ApicalV=table2array(ApicalV);
ApicalQ=readtable('TraubFIg7apicalq_vect.txt');
ApicalQ=table2array(ApicalQ);
SomaCxi=readtable('TraubFig7cxi_vect.txt');
SomaCxi=table2array(SomaCxi);
SomaH=readtable('TraubFig7h_vect.txt');
SomaH=table2array(SomaH);
SomaM=readtable('TraubFig7m_vect.txt');
SomaM=table2array(SomaM);
SomaN=readtable('TraubFig7n_vect.txt');
SomaN=table2array(SomaN);
SomaQ=readtable('TraubFig7q_vect.txt');
SomaQ=table2array(SomaQ);
SomaR=readtable('TraubFig7r_vect.txt');
SomaR=table2array(SomaR);
ApicalR=readtable('TraubFig7rapical.txt');
ApicalR=table2array(ApicalR);
SomaS=readtable('TraubFig7s_vect.txt');
SomaS=table2array(SomaS);
ApicalS=readtable('TraubFig7sapical.txt');
ApicalS=table2array(ApicalS);
SomaV=readtable('TraubFig7SomaV.txt');
SomaV=table2array(SomaV);

%Graphing Figure 7 From Traub et al 1991

figure
if ~verLessThan('matlab','9.5')
	sgtitle('Figure 7')
end

subplot(6,2,1)
plot(SomaV(:,1),SomaV(:,2))
ylim([-5 100])
ylabel('Membrane Potential (mV)')
title('Soma')

subplot(6,2,2)
plot(ApicalV(:,1),ApicalV(:,2))
ylim([-5 100])
title('Apical Dendrite 0.6 \lambda from soma')

subplot(6,2,3)
plot(SomaQ(:,1),SomaQ(:,2))
ylabel('q')
ylim([0 1])

subplot(6,2,4)
plot(ApicalQ(:,1),ApicalQ(:,2))
ylim([0 1])

subplot(6,2,5)
plot(SomaN(:,1),SomaN(:,2))
ylabel('n')
ylim([0 1])

subplot(6,2,7)
plot(SomaCxi(:,1),SomaCxi(:,2))
ylabel('C_X')
ylim([0 1])

subplot(6,2,8)
plot(ApicalCxi(:,1),ApicalCxi(:,2))
ylim([0 1])
title('All Channel Variables are normalized to 0-100% on the Y axis')


P=SomaS(:,2).^2.*SomaR(:,2);

subplot(6,2,9)
plot(SomaS(:,1),P)
ylabel('S^2r')
ylim([0 1])

L=ApicalS(:,2).^2.*ApicalR(:,2);

subplot(6,2,10)
plot(ApicalS(:,1), L)
ylim([0 1])

K=SomaM(:,2).^2.*SomaH(:,2);

subplot(6,2,11)
plot(SomaM(:,1),K)
ylabel('m^2h')
xlabel('Time (ms)') 
ylim([0 1])
