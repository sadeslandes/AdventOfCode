using System.CommandLine;
using System.Diagnostics;
using System.Text.RegularExpressions;
using aoc.EntryPoint;
using mazharenko.AoCAgent;
using mazharenko.AoCAgent.Base;

namespace AoC.Profiler;


class Program
{
    static async Task<int> Main(string[] args)
    {
        var rootCmd = new RootCommand("aoc-profiler");
        var repeatOption = new Option<int>(
            aliases: ["--repeat", "-n"],
            description: "Number of times to repeat execution",
            getDefaultValue: () => 100);
        var yearOption = new Option<int>(
            aliases: ["--year", "-y"],
            description: "Year of solution to profile",
            getDefaultValue: () => DateTime.Now.Year);
        var dayOption = new Option<string>(
            aliases: ["--day", "-d"],
            description: "Day of solution to profile");
        var partOption = new Option<string>(
            aliases: ["--part", "-p"],
            description: "Number of times to repeat execution");

        rootCmd.AddOption(repeatOption);
        rootCmd.AddOption(yearOption);
        rootCmd.AddOption(dayOption);
        rootCmd.AddOption(partOption);
        rootCmd.SetHandler(
            (numRepeats, year, day, part) =>
            {
                Console.WriteLine($"Profiling year {year} day(s): {day} part(s): {part}. Repeat: {numRepeats}");
                YearBase yearRunner;
                Stopwatch stopwatch = new();
                List<long> timings = new(capacity: numRepeats);

                switch (year)
                {
                    case 2023:
                        yearRunner = new Year2023();
                        break;
                    default:
                        throw new InvalidOperationException($"Invalid year {year} specified");
                }

                foreach (RunnerDay rd in yearRunner.Days)
                {
                    if (day != "all" && rd.Num != int.Parse(day))
                    {
                        continue;
                    }

                    string dayInput = File.ReadAllText($"inputs/input{rd.Num:00}.txt");
                    foreach (RunnerPart rp in new[] {rd.Part1, rd.Part2})
                    {
                        if (part != "all" && rp.Num != int.Parse(part))
                        {
                            continue;
                        }

                        for (int i = 0; i < numRepeats; i++)
                        {
                            try
                            {
                                stopwatch.Start();
                                rp.Part.SolveObtained(dayInput);
                                stopwatch.Stop();
                            }
                            catch (NotImplementedException)
                            {
                                return;
                            }
                            finally
                            {
                                stopwatch.Stop();
                            }
                            timings.Add(stopwatch.ElapsedTicks);
                            stopwatch.Reset();
                        }
                        var duration = TimeSpan.FromTicks((long)timings.Average());
                        if (duration.Seconds < 10)
                        {
                            Console.ForegroundColor = ConsoleColor.Green;
                        }
                        else
                        {
                            Console.ForegroundColor = ConsoleColor.Red;
                        }
                        Console.WriteLine($"Year {year}, Day {rd.Num}, Part {rp.Num}, {numRepeats} trials: {duration.TotalMilliseconds:.000}ms");
                        timings.Clear();
                        Console.ResetColor();
                    }
                }
            },
            repeatOption,
            yearOption,
            dayOption,
            partOption);
        return await rootCmd.InvokeAsync(args);
    }
}
