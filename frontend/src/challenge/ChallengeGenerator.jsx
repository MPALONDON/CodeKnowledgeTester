import "react";
import {useState, useEffect} from "react";
import MCQChallenge from "./MCQChallenge.jsx";
import styles from "./challenge.module.css";

export default function ChallengeGenerator(){
    const [challenge,setChallenge] = useState(null);
    const [isLoading,setIsLoading] = useState(false)
    const [error,setError] = useState(null)
    const [difficulty, setDifficulty] = useState("easy")
    const [quota, setQuota] = useState(null)

    const fetchQuota = async() => {}

    const generateChallenge = async() => {}

    function handleDifficulty(e){
        setDifficulty(e.target.value)
    }

    const getNextResetTime = () => {}
    return <div className={styles.challengeContainer}>
        <h2>Challenge Generator</h2>
        <div className={styles.quotaDisplay}></div>
        <p>Challenges remaining today: {quota?.quota_remaining || 0}</p>
        {quota?.quota_remaining === 0 && (
            <p>Next reset: {0}</p>
        )}
        <div className={styles.difficultySelector}>
            <label htmlFor="difficulty">Select Difficulty</label>
            <select id="difficulty"
                    value={difficulty}
                    onChange={handleDifficulty}
                    disabled={isLoading}>
                <option value="easy">Easy</option>
                <option value="medium">Medium</option>
                <option value="hard">Hard</option>
            </select>
        </div>
        <button
            onClick={generateChallenge}
            disabled={isLoading || quota?.quota_remaining === 0}
            className={styles.generateButton}
        >{isLoading ? "Generating..." : "Generate Challenge"}
        </button>

        {error && <div className={styles.errorMessage} >
            <p>{error}</p>
        </div>}
        {challenge && <MCQChallenge challenge={challenge}/>}

    </div>
}