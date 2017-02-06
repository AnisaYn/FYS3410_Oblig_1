% A test to calculate madelung constant from real space
% For Na Cl


n = 50; % layers in real space
V = 0;
n_list = [];
V_list = [];
for layer = 1:n
    for ni = -layer:layer
    for nj = -layer:layer
    for nk = -layer:layer
    nn_list = [ni nj nk];
    if ( max(abs(nn_list)) == layer )
        rij = (ni^2 + nj^2 + nk^2)^(0.5);
        if mod(ni + nj +nk, 2) == 1
            zj = -1;
        else 
            zj = 1;
        end
        V = V + zj / rij;
    end
    end
    end
    end
    layer
    V
    n_list = [n_list layer];
    V_list = [V_list V];
end
plot(n_list, V_list)

xlabel('Størrelse til krystallen','fontsize',16)
ylabel('Madelung Konstant', 'fontsize',16)
title('Madelung konstant som funksjon av krsytall størrelse', 'fontsize',18)
set(gca,'FontSize',18);