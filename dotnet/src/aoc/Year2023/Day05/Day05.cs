using System.Security.AccessControl;
using Spectre.Console.Rendering;

namespace aoc.Year2023.Day05;

internal partial class Day05
{
    private static (List<uint> seeds, List<SortedDictionary<uint, (uint end, uint dest)>> maps) ParseInput(string input)
    {
        var sections = input.Split("\n\n");
        var seeds = sections[0].Substring(7).Split(' ').Select(uint.Parse).ToList();
        List<SortedDictionary<uint, (uint end, uint dest)>> maps = new();

        foreach (var inputMap in sections.Skip(1))
        {
            SortedDictionary<uint, (uint end, uint dest)> map = new();
            foreach (var line in inputMap.Split("\n").Skip(1))
            {
                var values = line.Split(' ').Select(uint.Parse).ToArray();
                map.Add(values[1], (values[1] + values[2], values[0]));
            }
            maps.Add(map);
        }

        return (seeds, maps);
    }

    internal partial class Part1
    {
        private readonly Example example = new(
            """
            seeds: 79 14 55 13

            seed-to-soil map:
            50 98 2
            52 50 48

            soil-to-fertilizer map:
            0 15 37
            37 52 2
            39 0 15

            fertilizer-to-water map:
            49 53 8
            0 11 42
            42 0 7
            57 7 4

            water-to-light map:
            88 18 7
            18 25 70

            light-to-temperature map:
            45 77 23
            81 45 19
            68 64 13

            temperature-to-humidity map:
            0 69 1
            1 0 69

            humidity-to-location map:
            60 56 37
            56 93 4
            """,
            "35");

        public string Solve(string input)
        {
            (List<uint> seeds, List<SortedDictionary<uint, (uint end, uint dest)>> maps) = ParseInput(input);
            uint closest = uint.MaxValue;
            
            foreach (uint seed in seeds)
            {
                uint output = seed;
                foreach (var map in maps)
                {
                    foreach (var begin in map.Keys)
                    {
                        if (output < begin)
                        {
                            break;
                        }
                        else if (output < map[begin].end)
                        {
                            output = map[begin].dest + output - begin;
                            break;
                        }
                    }
                }
                closest = uint.Min(closest, output);
            }
            return closest.ToString();
        }
    }

    internal partial class Part2
    {
        private readonly Example example = new(
            """
            seeds: 79 14 55 13

            seed-to-soil map:
            50 98 2
            52 50 48

            soil-to-fertilizer map:
            0 15 37
            37 52 2
            39 0 15

            fertilizer-to-water map:
            49 53 8
            0 11 42
            42 0 7
            57 7 4

            water-to-light map:
            88 18 7
            18 25 70

            light-to-temperature map:
            45 77 23
            81 45 19
            68 64 13

            temperature-to-humidity map:
            0 69 1
            1 0 69

            humidity-to-location map:
            60 56 37
            56 93 4
            """,
            "46");

        public string Solve(string input)
        {
            throw new NotImplementedException();
        }
    }
}