%Soma filtros
function Fnovo = somaFiltros(F1,F2)
    A = F1(1)+F2(1);
    B(1) = 0;
    for i = 2:size(F1)
        B(i-1) = F1(i)+F2(i);
    end
    
    Fnovo(1) = A;
    for i=1:size(B)
        Fnovo(i+1) = B(i);
    end
end