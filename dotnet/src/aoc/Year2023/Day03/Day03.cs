using System.Collections.Generic;
using System.Diagnostics.Metrics;
using Spectre.Console.Rendering;

namespace aoc.Year2023.Day03;

internal partial class Day03
{
    record Point(int x, int y);

    class PotentialPartNumber
    {
        public PotentialPartNumber(int value) => Value = value;
        public int Value {get;}
    }

    private static IEnumerable<Point> GetAdjacent(Point o)
    {
        foreach (int dy in Enumerable.Range(-1,3))
        {
            foreach (int dx in Enumerable.Range(-1,3))
            {
                if (dy == 0 && dx == 0)
                {
                    continue;
                }
                yield return new Point(o.x + dx, o.y + dy);
            }
        }
    }

    private static (Dictionary<Point,char> Symbols, Dictionary<Point,PotentialPartNumber> PotentialPartNumbers) ParseInput(string input)
    {
        string numberBuffer = "";
        Dictionary<Point,char> symbols = new();
        Dictionary<Point,PotentialPartNumber> partNumbers = new();
        var lines = input.Split("\n");
        for (int y = 0; y < lines.Length; y++)
        {
            string line = lines[y];
            for (int x = 0; x < line.Length; x++)
            {
                char _char = line[x];
                if(char.IsNumber(_char))
                {
                    numberBuffer += _char;
                }
                else
                {
                    if (numberBuffer.Length > 0)
                    {
                        PotentialPartNumber ppn = new(int.Parse(numberBuffer));
                        for (int i = 0; i < numberBuffer.Length; i++)
                        {
                            partNumbers.Add(new Point(x - i - 1, y), ppn);
                        }
                        numberBuffer = string.Empty;
                    }

                    if (_char == '.')
                    {
                        continue;
                    }
                    else
                    {
                        symbols.Add(new Point(x,y), _char);
                    }
                }
            }

            if (numberBuffer.Length > 0)
            {
                PotentialPartNumber ppn = new(int.Parse(numberBuffer));
                for (int i = 0; i < numberBuffer.Length; i++)
                {
                    partNumbers.Add(new Point(line.Length - i - 1, y), ppn);
                }
                numberBuffer = string.Empty;
            }
        }
        return (symbols, partNumbers);
    }

    internal partial class Part1
    {
        private readonly Example example = new(
            """
            467..114..
            ...*......
            ..35..633.
            ......#...
            617*......
            .....+.58.
            ..592.....
            ......755.
            ...$.*....
            .664.598..
            """,
            "4361");

        private readonly Example example2 = new(
            """
            1.1
            .#.
            1.1
            """,
            "4");

        private readonly Example example3 = new(
            """
            .1.
            1#1
            .1.
            """,
            "4");

        private readonly Example example4 = new(
            """
            111
            1#1
            111
            """,
            "224");

        private readonly Example example5 = new(
            """
            .1.
            #.#
            """,
            "1");

        private readonly Example example6 = new(
            """
            1..
            ..#
            """,
            "0");

        private readonly Example example7 = new(
            """
            ###
            #1#
            ###
            """,
            "1");

        private readonly Example example8 = new(
            """
            1.1
            ###
            """,
            "2");

        private readonly Example example9 = new(
            """
            ..#
            11.
            """,
            "11");

        public string Solve(string input)
        {
            (Dictionary<Point,char> symbols, Dictionary<Point,PotentialPartNumber> potentialPartNumbers) = ParseInput(input);
            HashSet<PotentialPartNumber> counted = new();
            int sum = 0;
            foreach (var symbol in symbols)
            {
                foreach (var adj in GetAdjacent(symbol.Key))
                {
                    if (potentialPartNumbers.TryGetValue(adj, out PotentialPartNumber? pn) && !counted.Contains(pn))
                    {
                        sum += pn.Value;
                        counted.Add(pn);
                    }
                }
            }
            return sum.ToString();
        }
    }

    internal partial class Part2
    {
        private readonly Example example = new(
            """
            467..114..
            ...*......
            ..35..633.
            ......#...
            617*......
            .....+.58.
            ..592.....
            ......755.
            ...$.*....
            .664.598..
            """,
            "467835");
        public string Solve(string input)
        {
            (Dictionary<Point,char> symbols, Dictionary<Point,PotentialPartNumber> potentialPartNumbers) = ParseInput(input);
            HashSet<PotentialPartNumber> counted = new();
            int sum = 0;
            foreach (var gear in symbols.Where(s => s.Value == '*'))
            {
                foreach (var adj in GetAdjacent(gear.Key))
                {
                    if (potentialPartNumbers.TryGetValue(adj, out PotentialPartNumber? pn) && !counted.Contains(pn))
                    {
                        counted.Add(pn);
                    }
                }

                if (counted.Count == 2)
                {
                    sum += counted.Aggregate(1, (acc, pn) => acc * pn.Value);
                }
                counted.Clear();
            }
            return sum.ToString();
        }
    }
}