perc = [];
peri = [];
perfn = [];
perfp = [];
pertn = [];
pertp = [];

% i = 1;

% for i = 1:1000
    x = traininginputs';
    t = trainingtargets';

    net = patternnet(100);

    net.divideFcn = 'divideint';
    net.divideParam.trainRatio = 1;
    net.divideParam.valRatio = 1;
    net.divideParam.testRatio = 0;

    [net, tr] = train(net, x, t);

    testX = inputs';
    testT = targets';

    testY = net(testX);
    testIndices = vec2ind(testY);

%     plotconfusion(testT,testY);

    [c,cm] = confusion(testT,testY);

    fprintf('Percentage Correct Classification   : %f%%\n', 100*(1-c));
    fprintf('Percentage Incorrect Classification : %f%%\n', 100*c);
    
    perc(i) = 100*(1-c);
    peri(i) = 100*c;

    y = testY;
    t = testT;
    numSamples = size(t,2);
    [c,cm] = confusion(t,y);
    numColumns = 2;
    for j=1:numColumns
        for k=1:numColumns
            if (j==k)
                num = cm(j,k);
                top = num2str(num);
                per = num/numSamples;
%                 bottom = percent_string(perc);
                
                if j==1
                    % true negative
                    pertn(i) = per;
                elseif j==2
                    % true positive
                    pertp(i) = per;
                end
            else
                num = cm(j,k);
                top = num2str(num);
                per = num/numSamples;
%                 bottom = percent_string(perc);
                if j==1 && k==2
                    % false negative
                    perfn(i) = per;
                elseif j==2 && k==1
                    % false positive
                    perfp(i) = per;
                end
            end
        end
    end
% end

mean(perc)
min(perc)
max(perc)
mean(peri)
min(peri)
max(peri)