clear all

c1 = [1, 1, 1, 1, 1.05, 0.95]; 
c2 = [1, 1, 1.1, 1, 1, 0.9]; 
c3 = [1 ,0.92, 1, 1.05, 1, 1]; 

cc = [c1; c2; c3];

for ii = 1:3
 [firing_rate] = runModel(cc(ii,:));
end