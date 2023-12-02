using System.Linq;
using System.Text.RegularExpressions;

namespace aoc.Year2023.Day02;

internal partial class Day02
{
    record GameSet(int Red, int Green, int Blue);
    record Game(int Id, GameSet[] Sets);

    private static Game[] ParseInput(string input)
    {
        Regex rx = new Regex(@"(?<count>\d+) (?<color>blue|green|red)");
        return input.Split("\n").Select(line =>
        {
            var gameParts = line.Split(":");
            int gameId = int.Parse(gameParts[0].Substring(5));
            var gameSets = gameParts[1].Split(';')
                .Select(set =>
                {
                    var marbles = rx.Matches(set)
                        .ToDictionary(k => k.Groups["color"].Value, v => int.Parse(v.Groups["count"].Value));
                    return new GameSet(
                        Red: marbles.TryGetValue("red", out int r) ? r : 0,
                        Green: marbles.TryGetValue("green", out int g) ? g : 0,
                        Blue: marbles.TryGetValue("blue", out int b) ? b : 0);
                });
            return new Game(gameId, gameSets.ToArray());
        }).ToArray();
    }

    internal partial class Part1
    {
        private readonly Example ex = new(
            """
            Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
            Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
            Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
            Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
            Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
            """,
            "8");

        public string Solve(string input)
        {
            var games = ParseInput(input);
            var validGames = games.Where(g => g.Sets.All(s => s.Red <= 12 && s.Green <= 13 && s.Blue <= 14));
            return validGames.Sum(g => g.Id).ToString();
        }
    }

    internal partial class Part2
    {
        private readonly Example ex = new(
            """
            Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
            Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
            Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
            Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
            Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
            """,
            "2286");

        public string Solve(string input)
        {
            var games = ParseInput(input);
            return games.Sum(g => g.Sets.Max(s => s.Red) * g.Sets.Max(s => s.Green) * g.Sets.Max(s => s.Blue))
                .ToString();
        }
    }
}