%%Funcao para montar os filtros e deixa-los prontos para o uso
function [G, den] = montaFiltro(R)
    %separando as variaveis do filtro ressonante
    A = R(1);
    B = R(2);
    C = R(3);
    %%transformando o ganho de dB para valores de uso
    G = 10^(A/20);
    %%montando o vetor do denominador
    den(1) = 1;
    if (C~=0)
        den(3) = -C;
    end
    if (B~=0)
        den(2) = -B;
    end
end