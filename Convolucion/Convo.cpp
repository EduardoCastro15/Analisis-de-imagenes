#include <cstdlib>
#include <iostream>
#include <stdlib.h>
#include <time.h>

#define length(x) (sizeof(x)/sizeof(x[0]))

using namespace std;

int convolucion ()
{
    int mitad, i,j,m,n,mm,nn,ii,jj, acumulador;
    
    // Defino Kernel
    int kernel[3][3] = {
                        {1, 2, 1},
                        {2, 4, 2},
                        {1, 2, 1}
                    };
    // Defino Imagen
    int image[7][7] = { 
                        {5, 14, 0, 0, 56, 35, 42},
                        {0, 180, 180, 179, 79, 55, 47},
                        {1, 188, 0, 191, 50, 50, 10},
                        {193, 33, 215, 255, 160, 10, 0},
                        {100, 230, 0, 230, 190, 200, 200},
                        {0, 230, 200, 230, 190, 0, 200},
                        {0, 2, 2, 18, 12, 70, 0}
                    };     
    // Defino Imagen resultante
    int result[7][7]; 
    // Hallar la mitad del kernel para posicionar la matriz desde ahi
    
    mitad = length(kernel) / 2;
    
    /* Proceso de convolucion
     * Recorro la imagen en los dos primeros for, al igual que el kernel
     * en la variable mm hallo el indice de la fila del kernel alrevez, al
     * igual que la variable nn, almacena la columna del kernel alrevez,
     * las variables ii,jj son para almacenar la posicion de las imagenes tomando
     * en cuenta su limite exterior es decir i-1, j-1,la variable acumulador almacena el resultado
     * que luego es asignado en la posicion de la imagen resultante
     */   

    for (i = 0; i < length(image); ++i) // Filas
    {
        for (j = 0; j < length(image); ++j) // Columnas
        {
            // Variable acumuladora
            acumulador = 0;
            
            for (m = 0; m < length(kernel); ++m) // Filas del Kernel
            {
                mm = length(kernel) - 1 - m; // Indice de la fila del kernel alrevez

                for (n = 0; n < length(kernel); ++n) // Columnas del kernel
                {
                    nn = length(kernel) - 1 - n; // Indice de la columna del kernel alrevez

                    
                    ii = i + (m - mitad);
                    jj = j + (n - mitad);

                    // validar limites de la imagen 00000
                    if (ii >= 0 && ii < length(image) && jj >= 0 && jj < length(image))
                    {
                        acumulador += image[ii][jj] * kernel[mm][nn];
                    }                        
                }
            }
            result[i][j] = acumulador/16;
        }
    }
    
    // Muestro imagen final aplicando la convolucion
    cout<<endl<<endl<<"Imagen Aplicando convolucion: "<<endl;
    for(int i = 0; i < length(result); i++)
    {
        for(int j = 0; j < length(result); j++)
        {
            cout<<" "<<result[i][j];            
        }
        cout<<endl;
    }
    
    return 0;

}

int main(int argc, char** argv) {

    convolucion();
    
    return 0;
}
