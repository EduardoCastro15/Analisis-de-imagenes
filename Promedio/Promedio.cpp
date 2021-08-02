#include <stdio.h>
#include <stdlib.h>
#include<math.h>

int main(void)
{
	float **a,*b,r,promedio=0.0,total,tamano,varianza=0.0,sub,frac;
	int n,m,i,j,k,l,aux,z;
	
	printf("Ingresa el numero de filas: ");								
	scanf ("%i", &m);
	printf("Ingresa el numero de columnas: ");
	scanf ("%i", &n);												//definicion de tamaños
	a=(float**) malloc(m*sizeof(float*));
	 for(i=0;i<n;i++)
	 {
	 	a[i]=(float*)malloc(n*sizeof(float*));					//creacion del arreglo
	 }
	b=(float*)malloc(256*sizeof(float*));
	 for(i=0;i<n;i++)
	 {
	 	for(j=0;j<m;j++)
	 	{
	 		printf("Ingresa el numero de la fila %i y columna %i: ",i,j);
			scanf ("%f", &r);
	 		a[i][j]=r;															//LLenado del arreglo manual
		}
	 }
	  for(i=0;i<n;i++)
	 {
	 	for(j=0;j<m;j++)
	 	{
	 		printf("a[%i][%i]: %.1f\t",i,j,a[i][j]);		//impresion del arreglo
		}
		printf("\n");
	 }
	 printf("\n\n\n");
	/*for(i=0;i<n;i++)										//ordenar el arreglo
     {
        for(j=0;j<m;j++)
        {
            for(k=0;k<n;k++)
            {
                for(l=0;l<m;l++)
                {
                    if(a[i][j]<a[k][l])
                    {
                        aux=a[i][j];
                        a[i][j]=a[k][l];
                        a[k][l]=aux;
                    }
 
                }
            }
         }
    }
	 for(i=0;i<n;i++)
	 {
	 	for(j=0;j<m;j++)
	 	{
	 		printf("a[%i][%i]: %f\t",i,j,a[i][j]);										//Nueva impresion de arreglo ordenado
		}
		printf("\n");
	 }*/
	for(i=0;i<n;i++)										//promedio o media
     {
        for(j=0;j<m;j++)
        {
            promedio+=a[i][j];
        }
    }
    tamano=n*m;
    total=promedio/tamano;
    printf("\nLa suma es: %f\n El tamano es de %f\n El promedio es de: %.2f\n",promedio,tamano, total);
    ///////////////////////////////////////////////////////////////////////////////////////////////////
   for (i = 0; i <= 256; i++)										//cuenta la repeticion de cada valor del 0 al 255
   {
   		b[i] = 0.0;	
   }
 
   for (i = 0; i < m; i++)
	{
		for (j=0;j<n;j++)
		{
		    for (z = 0; z <= 256; z++)
		      {
		         if (a[i][j] == z)
		         {
		          b[z]++;
		         }
		      }
		}
   }
 
   printf ("\n");

   for (i = 0; i <= 256; i++)
   {
       if (b[i] != 0.0)
       {
          printf ("%d se repite %.1f veces\n", i, b[i]);							//muestra las repeticiones de cada valor que aparece en la tabla y va 
          sub=pow((i-total),2);														//haciendo la sumatoria de varianza
          frac=b[i]/tamano;
          varianza+=(sub*frac);
       }
   }
   printf ("\nLa varianza es: %.2f\n",varianza);
   getchar();
	return 0;
}
