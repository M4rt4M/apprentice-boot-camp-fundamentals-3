package toggle;

public class BowlingCalculator {
    private final boolean spareScoring;

    public BowlingCalculator() {
        this(false);
    }

    BowlingCalculator(boolean spareScoring) {
        this.spareScoring = spareScoring;
    }

    public int score(int... bowls) {
        int score = 0;
        if (spareScoring) {
            // Work in progress
            for (int bowl = 0; bowl < bowls.length; bowl++) {
                if (bowl >= 2 && bowls[bowl - 1] + bowls[bowl - 2] == 10) {
                    score += bowls[bowl];
                }
                score += bowls[bowl];
            }
        } else {
            for (int bowl : bowls) {
                score += bowl;
            }
        }
        return score;
    }
}
