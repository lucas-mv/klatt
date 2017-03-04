%Funcao para aplicar um ganho externo a um filtro
function data = ganhoExterno(x, A)
    data(1) = 0;
    G = 10^(A/20);
    for i=1:size(x)
        data(i) = x(i)*G;
    end
end