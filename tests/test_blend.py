from letterboxd_blend.blend import candidates
from letterboxd_blend.models import Movie, Profile


def test_candidates_excludes_watched_by_either_person():
    a_movie = Movie("lb/a", "A")
    b_movie = Movie("lb/b", "B")
    unseen = Movie("lb/c", "C")

    alice = Profile("alice", watched={a_movie})
    bob = Profile("bob", watched={b_movie})

    assert candidates(alice, bob, {a_movie, b_movie, unseen}) == {unseen}
