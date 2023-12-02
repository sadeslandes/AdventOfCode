using mazharenko.AoCAgent.Generator;

namespace AoC.Tests;

[TestFixture]
[GenerateInputTests(2023, nameof(GetCases))]
internal partial class InputTests
{
    private static IEnumerable<PartInputCaseData> GetCases()
    {
        yield return new PartInputCaseData(1, 1, "54450");
        yield return new PartInputCaseData(1, 2, "54265");
        yield return new PartInputCaseData(2, 1, "2486");
        yield return new PartInputCaseData(2, 2, "87984");
    }
}