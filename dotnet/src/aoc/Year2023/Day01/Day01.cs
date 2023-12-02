using System.Linq;

namespace aoc.Year2023.Day01;

internal partial class Day01
{
    private static int ExtractFirstLastNumbers(string input)
    {
        var numbers = input.Where(c => char.IsNumber(c));
        return int.Parse(string.Concat(numbers.First(), numbers.Last()));
    }

    private static string ReplaceTextWithNumber(string input)
    {
        return input
            .Replace("one", "one1one")
            .Replace("two", "two2two")
            .Replace("three", "three3three")
            .Replace("four", "four4four")
            .Replace("five", "five5five")
            .Replace("six", "six6six")
            .Replace("seven", "seven7seven")
            .Replace("eight", "eight8eight")
            .Replace("nine", "nine9nine");
    }

    internal partial class Part1
    {
        private readonly Example ex = new(
            """
            1abc2
            pqr3stu8vwx
            a1b2c3d4e5f
            treb7uchet
            """,
            "142");

        public string Solve(string input)
        {
            var calibrationValues = input.Split("\n").Select(ExtractFirstLastNumbers);
            return calibrationValues.Sum().ToString();
        }
    }
    internal partial class Part2
    {
        private readonly Example ex = new(
            """
            two1nine
            eightwothree
            abcone2threexyz
            xtwone3four
            4nineeightseven2
            zoneight234
            7pqrstsixteen
            """,
            "281");

        public string Solve(string input)
        {
            var preProcessed = input.Split("\n").Select(ReplaceTextWithNumber);
            var calibrationValues = preProcessed.Select(ExtractFirstLastNumbers);
            return calibrationValues.Sum().ToString();
        }
    }
}
