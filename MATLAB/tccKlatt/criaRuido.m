%%Funcao para criar o ruido a ser adicionado
function noise = criaRuido(Ta, t_sintese, A)
    %Numero de amostras
    N = ceil(t_sintese/Ta);
    n = rand(1,N);
    %n = zeros(1,N);
    %noise = n*(10^(A/20));
    noise = n;
    
    %efeito do LPF
    %noise = filter([1], [1 -1],noise);
    %noise = filter(1, [0.00000000000000001 1], noise);
    
    %Normalizando os valores para somar com o resultado de RGZ + RGS
    M = max(noise);
    noise = noise/M;
end