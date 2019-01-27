using System;

namespace _941.Difference
{
    class Program
    {
        static void Main(string[] args)
        {
            int eded = Math.Abs(Convert.ToInt32(Console.ReadLine()));
            int yuzluk = eded / 100;
            int onluq = (eded / 10) % 10;
            int teklik = eded % 10;
            int cem = yuzluk + onluq + teklik;
            int hasil = yuzluk * onluq * teklik;
            Console.WriteLine(hasil - cem);
            Console.ReadKey();
        }
    }
}
