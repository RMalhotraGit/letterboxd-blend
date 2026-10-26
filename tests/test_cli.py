from letterboxd_blend.cli import main


def test_cli_runs(capsys):
    assert main(["a_export", "b_export", "-n", "5"]) == 0
    assert "top 5" in capsys.readouterr().out
