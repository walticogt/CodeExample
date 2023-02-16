using System;

namespace EsPar_Impar
{
    class Program
    {
        static void Main(string[] args)
        {
            int numero;
            string resultado;

            Console.Write("Ingrese un número: ");
            numero = Convert.ToInt32(Console.ReadLine());

            if (numero % 2 == 0)
            {
                resultado = "Es Par";
            }
            else
            {
                resultado = "Es Impar";
            }

            Console.WriteLine(resultado);
        }
    }
}

