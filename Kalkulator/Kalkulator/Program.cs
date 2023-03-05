using System;
class Kalkulator
{
	static void Main(string[] args)
	{
		Console.WriteLine("1 = dodawanie 2 = odejmowanie 3 = dzielenie 4 = mnożenie");
		var inp = Console.ReadLine();
		int liczbaq = int.Parse(Console.ReadLine());
		int liuczbaw = int.Parse(Console.ReadLine());
		switch(inp)
		{
			case "1":
				Console.WriteLine(liczbaq + liuczbaw);
				break;
			case "2":
				Console.WriteLine(liczbaq - liuczbaw);
				break;
			case "3":
				Console.WriteLine(liczbaq / liuczbaw);
				break;
			case "4":
				Console.WriteLine(liczbaq * liuczbaw);
				break;
			default:
				Console.WriteLine("There is no such operation");
				break;
		}
		Console.ReadKey();

	}
}

