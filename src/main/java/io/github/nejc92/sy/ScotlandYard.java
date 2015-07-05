package io.github.nejc92.sy;

import io.github.nejc92.mcts.Mcts;
import io.github.nejc92.sy.game.Action;
import io.github.nejc92.sy.game.board.Board;
import io.github.nejc92.sy.game.State;
import io.github.nejc92.sy.players.Player;

public class ScotlandYard {

    public static void main(String... args) {
        Mcts<State, Action, Player> mcts = Mcts.initializeIterations(500);
        mcts.dontClone(Board.class);
        Player[] players = initializePlayers();
        State state = State.initialize(players);
        while (!state.isTerminal()) {
            state.setCurrentPlayerAsSearchInvokingPlayer();
            Action mostPromisingAction;
            if (state.currentPlayerIsHuman())
                break;
            else {
                mostPromisingAction = mcts.uctSearchWithExploration(state, 0.4);
                state.setSearchModeOff();
                state.performActionForCurrentAgent(mostPromisingAction);
            }
        }
    }

    private static Player[] initializePlayers() {
        return null;
    }
}