x = inputs';
t = results';

net = patternnet(10);
view(net)

net.divideFcn = 'divideint';
net.divideParam.trainRatio = 4/6;
net.divideParam.valRatio = 1/6;
net.divideParam.testRation = 1/6;

[net, tr] = train(net, x, t);
nntraintool