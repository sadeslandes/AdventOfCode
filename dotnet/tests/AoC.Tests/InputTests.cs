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
        yield return new PartInputCaseData(3, 1, "528819");
        yield return new PartInputCaseData(3, 2, "80403602");
        yield return new PartInputCaseData(4, 1, "24848");
        yield return new PartInputCaseData(4, 2, "7258152");
        yield return new PartInputCaseData(5, 1, "");
        yield return new PartInputCaseData(5, 2, "");
        yield return new PartInputCaseData(6, 1, "");
        yield return new PartInputCaseData(6, 2, "");
    }
}