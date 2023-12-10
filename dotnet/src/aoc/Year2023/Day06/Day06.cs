using mazharenko.AoCAgent.Generator;
using Spectre.Console;

namespace aoc.Year2023.Day06;

record Race(double Time, double Distance);

internal partial class Day06
{
    private static (double low, double high) GetTimeBounds(Race race)
    {
        return (
            Math.Floor(
                ((race.Time - Math.Sqrt((race.Time * race.Time) - (4 * race.Distance))) / 2) + 1),
            Math.Ceiling(
                ((race.Time + Math.Sqrt((race.Time * race.Time) - (4 * race.Distance))) / 2) - 1));
    }

    internal partial class Part1
    {
        private static IEnumerable<Race> ParseInput(string input)
        {
            var lines = input.Split("\n");
            var times = lines[0].Substring(6).Split("  ", StringSplitOptions.RemoveEmptyEntries);
            var distances = lines[1].Substring(10).Split("  ", StringSplitOptions.RemoveEmptyEntries);
            return times.Zip(distances).Select(z => new Race(double.Parse(z.First), double.Parse(z.Second)));
        }

        private readonly Example example = new(
            """
            Time:      7  15   30
            Distance:  9  40  200
            """,
            "288");

        public string Solve(string input)
        {
            var races = ParseInput(input);
            double result = 1;
            foreach (var race in races)
            {
                (double low, double high) = GetTimeBounds(race);
                result *= high - low + 1;
            }
            return result.ToString();
        }
    }

    internal partial class Part2
    {
        private static Race ParseInput(string input)
        {
            var lines = input.Split("\n");
            var time = lines[0].Substring(6).Replace(" ", "");
            var distance = lines[1].Substring(10).Replace(" ", "");
            return new Race(double.Parse(time), double.Parse(distance));
        }

        private readonly Example example = new(
            """
            Time:      7  15   30
            Distance:  9  40  200
            """,
            "71503");

        public string Solve(string input)
        {
            var race = ParseInput(input);
            (double low, double high) = GetTimeBounds(race);
            double result = high - low + 1;
            return result.ToString();
        }
    }
}