%%Funcoes para os coeficientes dos filtros do sintetizador de Klatt
function C = calculaCoefsResonatorAB (A,B)
    C = 1 -A -B;
end