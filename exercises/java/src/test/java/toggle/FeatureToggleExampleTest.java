package toggle;

import org.junit.Ignore;
import org.junit.Test;

import static org.assertj.core.api.Assertions.*;

public class FeatureToggleExampleTest {

    @Test
    public void simpleScoring() {
        BowlingCalculator bowlingCalculator = new BowlingCalculator(false);
        assertThat(bowlingCalculator.score(0,0,0,0,0,0)).isEqualTo(0);
        assertThat(bowlingCalculator.score(1,1,1,1,1,1)).isEqualTo(6);
        assertThat(bowlingCalculator.score(5,5,5,5,5,5)).isEqualTo(30);
    }
    
    @Test
    @Ignore
    public void spareScoring() {
        BowlingCalculator bowlingCalculator = new BowlingCalculator(true);
        assertThat(bowlingCalculator.score(5,5,5,5,5,5)).isEqualTo(40);
    }
}
