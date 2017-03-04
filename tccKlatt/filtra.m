%%Funcao para filtrar os dados pelo filtro desejado
function y = filtra(R, data)
    [G, den] = montaFiltro(R);
    y = filter(G, den, data);
end