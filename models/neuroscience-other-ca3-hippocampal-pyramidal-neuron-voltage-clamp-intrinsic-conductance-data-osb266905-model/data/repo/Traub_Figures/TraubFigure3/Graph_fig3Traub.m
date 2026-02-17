% Graph_Traub_Fig3

soma=importdata("iSomafig3.txt");
apical3=importdata("iApical3fig3.txt");
apical6=importdata("iApical6fig3.txt");
diam_soma=4.23*2; %um
[R C]=size(soma);

L_soma=125;  %um All length variables in um
soma_area=3320;  %All areas from Traub et al 1991
apical_area=2188;

%No need to adjust units, current outputted by neuron is always in mA/cm^2
%unless it is a point process

%10^3 multiplication needed to transform mA to uA
soma=(soma.*10^3);
apical3=(apical3.*10^3);
apical6=(apical6.*10^3);

Curve_int=floor(R/5);

dv=1;

figure
ah1 = subplot(3,1,1);
hold on
ylim(ah1,[-800 1300])
xlim(ah1,[-25 100])
yticks(ah1,-600:200:1200)
title(ah1,'Apical Dendrite 0.6\lambda')

ah2 = subplot(3,1,2)
hold on
ylim(ah2, [-100 1600])
xlim(ah2, [-25 100])
yticks(ah2, 0:200:1600)
title(ah2, 'Apical Dendrite 0.3\lambda')

ah3 = subplot(3,1,3)
hold on
ylabel(ah3, 'Current Density (uA/cm^2)')
xlabel(ah3,'Membrane Potential (mV Relative to Rest)')
ylim(ah3,[-700 1600])
xlim(ah3,[-25 100])
yticks(ah3,-600:200:1600)
title(ah3,'Soma')

for i=0:5
    plot(ah1, -25+dv:dv:100-dv,apical6((125*i)+1:125*(i+1)-1,1)')
    
    plot(ah2, -25+dv:dv:100-dv,apical3((125*i)+1:125*(i+1)-1,1)')
    
    plot(ah3, -25+dv:dv:100-dv,soma((125*i)+1:125*(i+1)-1,1)')
    
end

legend(ah1, 'cai=0', 'cai=50', 'cai=100', 'cai=150', 'cai=200', 'cai=250')

