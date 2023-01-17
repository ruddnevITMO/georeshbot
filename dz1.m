function []=dz1(theid, f5, g5, e106, e116, e126, x6, e206, e216, e226)
    thefile = append("id", int2str(theid), ".txt");
    fid = fopen(thefile, 'w');
    clc
    %% task5
    %f1 = [1 -1 3];
    %g1 = [5 1 6];
    v=[];
    Flag = 0;
    for i=0:20
        for j=0:20
            for k=0:20
                a=[[i, j, k]; f5; g5];
                if (i~=0 && j~=0 && k~=0) && (det(a)~=0)
                    v = [i, j, k];
                    Flag = 1;
                    break;
                end
                if Flag
                    break
                end
            end
            if Flag
                break
            end
        end
        if Flag
            break
        end
    end
    str = geolin(v);
    if str=="["
        str="[]";
    end
    fwrite(fid, unicode2native(char(">🦾 *Задача* 5>"), 'UTF-8'), 'uint8');
    fwrite(fid, unicode2native(char(str), 'UTF-8'), 'uint8');
    %% task6
    x = x6.';
    e0 = e206.';
    e1 = e216.';
    e2 = e226.';
    e3 = e106.';
    e4 = e116.';
    e5 = e126.';
    un1 = [e0 e1 e2];
    un2 = [e3 e4 e5];
    un2 = inv(un2);
    un = un2*un1*x;
    str = geolin(un.');
    if str=="["
        str="[]";
    end
    
    fwrite(fid, unicode2native(char(">>🦾 *Задача* 6>"), 'UTF-8'), 'uint8');
    fwrite(fid, unicode2native(char(str), 'UTF-8'), 'uint8');
    fclose(fid);
