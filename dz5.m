function []=dz5(theid, v11, v21, v31, u11, u21, v12, v22, v32, u12, u22, v13, v23, v33, u13, u23, v14, v24, v34, u14, u24)
    thefile = append("id", int2str(theid), ".txt");
    fid = fopen(thefile, 'w');
        
    clc
    %% task1
    disp("task1");
    % v1 = [-4 -3 8 11];
    % v2 = [-3 -2 6 8];
    % v3 = [1 1 -4 -4];
    % u1 = [1 1 -3 -3];
    % u2 = [-3 -3 9 10];
    
    un = [v11; v21; v31; u11; u21];
    un = rref(un);
    str = geolin(un);
    if str=="["
        str="[]";
    end
    fwrite(fid, unicode2native(char(">🦾 *Задача* 1>"), 'UTF-8'), 'uint8');
    fwrite(fid, unicode2native(char(str), 'UTF-8'), 'uint8');
    %% task2
    disp("task2");

    un = [v12; v22; v32; u12; u22];
    un = rref(un);
    str = geolin(un);
    if str=="["
        str="[]";
    end
    fwrite(fid, unicode2native(char(">>🦾 *Задача* 2>"), 'UTF-8'), 'uint8');
    fwrite(fid, unicode2native(char(str), 'UTF-8'), 'uint8');
    %% task3
    disp("task3");
    % v1 = [0 1 -1 2];
    % v2 = [1 -1 0 -1];
    % v3 = [7 -4 -2 -2];
    % u1 = [1 0 -1 1];
    % u2 = [-3 1 2 -1];
    
    % v1 = [2 4 -1 -8];
    % v2 = [0 -3 3 3];
    % v3 = [0 -1 1 1];
    % u1 = [2 3 1 -8];
    % u2 = [-6 -8 -3 22];
    % 
    % 
    % v1=[-3, 13, -11, 2];
    % v2=[6, -24, 18, -3];
    % v3=[-4, 16, -12, 2];
    % u1=[0, -2, 3, 0];
    % u2=[1, -4, 3, 0];
    
    % v1=[0 -1 1 0];
    % v2=[3 4 -10 -2];
    % v3=[-7 -8 22 5];
    % u1=[2 2 -6 0];
    % u2=[3 3 -9 0];
    % 
    % v1=[0 0 -2 3];
    % v2=[0 0 4 -6];
    % v3=[-2 5 8 -22];
    % u1=[-1 2 3 -8];
    % u2=[-1 3 1 -8];
    
    % v1=[-1 2 -1 2];
    % v2=[3 -4 1 -4];
    % v3=[-4 5 -1 5];
    % u1=[-2 -1 4 -2];
    % u2=[-4 -2 8 -4];
    %  un = [v1; v2; v3 ;u1 ; u2];
    % un = rref(un);
    % geolin(un);
    un1 = [v13; v23; v33];
    un2 = [u13; u23];
    % disp(un1);
    % disp(un2);
    un1 = delemptys(rref(un1));
    un2 = delemptys(rref(un2));
    % disp(un1);
    % disp(un2);
    un1 = FSR(un1);
    un2 = FSR(un2);
    un = [un1; un2];
    disp(un1);
    disp(un2);
    un = delemptys(rref(un));
    disp(un);
    un = FSR(un);
    %disp(un);
    str = geolin(un);
    str3 = geolin(un*3);
    
    fwrite(fid, unicode2native(char(">>🦾 *Задача* 3>"), 'UTF-8'), 'uint8');
    if str=="["
        str="[]";
        fwrite(fid, unicode2native(char(str), 'UTF-8'), 'uint8');
    else
        if str3=="["
            str3="[]";
        end
        fwrite(fid, unicode2native(char(str), 'UTF-8'), 'uint8');
        fwrite(fid, unicode2native(char(">или>"), 'UTF-8'), 'uint8');
        fwrite(fid, unicode2native(char(str3), 'UTF-8'), 'uint8');
    end
    % dim = size(un);
    % result = zeros((dim(2)-dim(1)),4);
    % un = FSR(un)
    % for i=1:(dim(2)-dim(1))
    %     fsr = un(:,(dim(2)-i+1));
    %     result(i, :) = fsr(1).*v1 + fsr(2).*v2 + fsr(3).*v3;
    % end
    % geolin(result);
    %% task4
    disp("task4");
    un = [v14; v24; v34; u14; u24];
    un = rref(un);
    str = geolin(un);
    if str=="["
        str="[]";

    end

    fwrite(fid, unicode2native(char(">>🦾 *Задача* 4>"), 'UTF-8'), 'uint8');

    fwrite(fid, unicode2native(char("Для суммы: >"), 'UTF-8'), 'uint8');

    fwrite(fid, unicode2native(char(str), 'UTF-8'), 'uint8');
    
    un1 = [v14; v24; v34];
    un2 = [u14; u24];
    un1 = delemptys(rref(un1));
    un2 = delemptys(rref(un2));
    un1 = FSR(un1);
    un2 = FSR(un2);
    un = [un1; un2];
    disp(un1);
    disp(un2);
    un = delemptys(rref(un));
    disp(un);
    un = FSR(un);
    str = geolin(un);
    str3 = geolin(un*3);
    fwrite(fid, unicode2native(char(">>Для пересечения: >"), 'UTF-8'), 'uint8');

    if str=="["
        str="[]";
        fwrite(fid, unicode2native(char(str), 'UTF-8'), 'uint8');
    else
        if str3=="["
            str3="[]";
        end
        fwrite(fid, unicode2native(char(str), 'UTF-8'), 'uint8');
        fwrite(fid, unicode2native(char(">или>"), 'UTF-8'), 'uint8');
        fwrite(fid, unicode2native(char(str3), 'UTF-8'), 'uint8');
    end

    fclose(fid);