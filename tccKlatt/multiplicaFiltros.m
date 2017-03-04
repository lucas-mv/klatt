%Funcao para multiplicar dois filtros
function Fnovo = multiplicaFiltros(F1, F2)
    A = F1(1)*F2(1);
    %criando vetores auxiliares
    F12 = F1(2:end);
    F22 = F2(2:end);
    B = conv(F12,F22);
    
    Fnovo(1) = A;
    for i=1:size(B)
        Fnovo(i+1) = B(i);
    end
end