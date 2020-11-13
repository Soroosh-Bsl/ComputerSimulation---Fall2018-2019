%RUN Q2.slx via Simulink

meanUtilOne = mean(UtilOne);
meanUtilTwo = mean(UtilTwo);
meanUtilThree = mean(UtilThree);
meanUtilFour = mean(UtilFour);
meanUtilFive = mean(UtilFive);

int = 2;
serv = 3;
n = 5;

modelUtil = min(1, (int ^ (-3))*(serv^(2)));
dataUtil = mean([meanUtilOne, meanUtilTwo, meanUtilThree, meanUtilFour, meanUtilFive]);
varianceDataUtil = var([meanUtilOne, meanUtilTwo, meanUtilThree, meanUtilFour, meanUtilFive]);

T = (modelUtil - dataUtil)/(sqrt(varianceDataUtil)/sqrt(n));
P = 1 - tcdf(T, n-1);

if P < 0.1
    disp("Rejected");
else
    disp("Not Rejected");
end