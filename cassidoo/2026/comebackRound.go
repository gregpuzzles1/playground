// Cassidoo question of the week:
// November 9th, 2026
//
// Question:
// Given rounds in a board game, where rounds[r][p] is the
// points player p earned in round r, find the earliest round
// from which the eventual winner is the sole leader at the
// end of every remaining round.
// Return the round number (1-based), or -1 if the final
// score is tied.

package main

import "fmt"

func comebackRound(rounds [][]int) int {
	if len(rounds) == 0 || len(rounds[0]) == 0 {
		return -1
	}

	totals := make([]int, len(rounds[0]))

	// Calculate each player's final score.
	for _, round := range rounds {
		for player, points := range round {
			totals[player] += points
		}
	}

	// Find the eventual winner.
	winner := 0
	for player := range totals {
		if totals[player] > totals[winner] {
			winner = player
		}
	}

	// Return -1 if the final winning score is tied.
	for player, score := range totals {
		if player != winner && score == totals[winner] {
			return -1
		}
	}

	// Reset the totals to examine the running scores.
	for player := range totals {
		totals[player] = 0
	}

	lastNotAhead := 0

	for r, round := range rounds {
		// Add this round's points to the running totals.
		for player, points := range round {
			totals[player] += points
		}

		// Check whether the winner is tied or behind.
		for player, score := range totals {
			if player != winner && score >= totals[winner] {
				lastNotAhead = r + 1
				break
			}
		}
	}

	return lastNotAhead + 1
}

func main() {
	fmt.Println(comebackRound([][]int{
		{5, 3, 2},
		{0, 5, 2},
		{4, 2, 2},
		{1, 3, 0},
	})) // Expected: 2

	fmt.Println(comebackRound([][]int{
		{4, 2},
		{1, 3},
		{2, 1},
	})) // Expected: 3

	fmt.Println(comebackRound([][]int{
		{4, 2},
		{1, 3},
	})) // Expected: -1
}
