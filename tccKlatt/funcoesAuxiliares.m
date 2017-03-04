%%Funcoes para os coeficientes dos filtros do sintetizador de Klatt
function [A, B, C] = calculaCoefsResonator(Fr, Ta, BW)
    C = -exp(-2*pi*BW*Ta);
    B = 2*exp(-pi*BW*Ta)*cos(2*pi*Fr*Ta);
    A = 1 -B -C;
end

function C = calculaCoefsResonatorAB (A,B)
    C = 1 -A -B;
end

%Funcao para multiplicar dois filtros
function Fnovo = multiplicaFiltros(F1, F2)
    A = F1(1)*F2(1);
    %criando vetores auxiliares
    F12 = F1[2:end];
    F22 = F2[2:end];
    B = conv(F12,F22);
    
    Fnovo(1) = A;
    for i=1:size(B)
        Fnovo(i+1) = B(i);
    end
end

%Multiplica o ganho do filtro
function Fnovo = multiplicaGanho(F,G)
    Fnovo = F;
    Fnovo(1) = F(1)*G;
end

%Soma filtros
function Fnovo = somaFiltros(F1,F2)
    A = F1(1)+F2(1);
    for i = 2:size(F1)
        B(i-1) = F1(i)+F2(i);
    end
    
    Fnovo(1) = A;
    for i=1:size(B)
        Fnovo(i+1) = B(i);
    end
end