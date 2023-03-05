using System;
using System.Reflection.Metadata;

class Qwqwq
{
    static void Main(string[] args)
    {
        Console.WriteLine("1 = obw kola 2 = pole kola 3 = pole kwadratu 4 = v kuli 5 = pole kuli 6 = pole walca 7 = v walca ");
        var inp = Console.ReadLine();
        int wybor = int.Parse(Console.ReadLine());
        switch (inp)
        {
            case "1":
                int r = int.Parse(Console.ReadLine());
                
                Console.WriteLine($"Wynik wynosi {2 * r * 3,14}");
                break;
            case "2":
                int qr = int.Parse(Console.ReadLine());

                Console.WriteLine($"Wynik wynosi {qr * qr * 3,14}");
                break;
            case "3":
                int a = int.Parse(Console.ReadLine());
                Console.WriteLine($"Wynik wynosi {a*a} ");
                break;
            case "4":
                int wr = int.Parse(Console.ReadLine());
                Console.WriteLine($"Wynik wynosi {wr * wr * wr * 3,14 * 3 / 4}");
                break;
            case "5":
                int er = int.Parse(Console.ReadLine());
                Console.WriteLine($"Wynik wynosi {er * er * 4 * 3,14}");
                break;
            case "6":
                int rr = int.Parse(Console.ReadLine());
                int h = int.Parse(Console.ReadLine());
                Console.WriteLine($"Wynik wynosi {rr * rr * h * 3,14}");
                break;
            case "7":
                int tr = int.Parse(Console.ReadLine());
                int qh = int.Parse(Console.ReadLine());
                Console.WriteLine($"Wynik wynosi {tr * tr * qh + qh * tr * 2 * 3,14}");
            default:
                Console.WriteLine("There is no such operation");
                break;
        }
        Console.ReadKey();

    }
}