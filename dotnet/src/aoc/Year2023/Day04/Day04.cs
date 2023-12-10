namespace aoc.Year2023.Day04;

internal partial class Day04
{
    record Card(int Id, int[] Winning, int[] Picked);

    private static IEnumerable<Card> ParseInput(string input)
    {
        foreach (string line in input.Split("\n"))
        {
            var lineParts = line.Split(':');
            int id = int.Parse(lineParts[0].Substring(5));
            var numberParts = lineParts[1].Split('|');
            var winning = numberParts[0].Split(' ', StringSplitOptions.RemoveEmptyEntries).Select(x => int.Parse(x));
            var picked = numberParts[1].Split(' ', StringSplitOptions.RemoveEmptyEntries).Select(x => int.Parse(x));
            yield return new Card(id, winning.ToArray(), picked.ToArray());
        }
    }

    internal partial class Part1
    {
        private readonly Example ex = new(
            """
            Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
            Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
            Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
            Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
            Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
            Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
            """,
            "13");

        public string Solve(string input)
        {
            int sum = 0;
            foreach (Card card in ParseInput(input))
            {
                var matches = card.Winning.Intersect(card.Picked);
                if (matches.Any())
                {
                    sum += (int)Math.Pow(2, matches.Count() - 1);
                }
            }
            return sum.ToString();
        }
    }

    internal partial class Part2
    {
        private readonly Example ex = new(
            """
            Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
            Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
            Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
            Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
            Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
            Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
            """,
            "30");

        public string Solve(string input)
        {
            Card[] cards = ParseInput(input).ToArray();
            int[] counts = new int[cards.Length];
            foreach (Card card in cards)
            {
                counts[card.Id - 1] += 1;
                var matches = card.Winning.Intersect(card.Picked);
                for (int i = 0; i < matches.Count(); i++)
                {
                    counts[card.Id + i] += counts[card.Id - 1];
                }
            }
            return counts.Sum().ToString();
        }
    }
}