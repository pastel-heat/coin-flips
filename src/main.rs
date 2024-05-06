use rand::Rng;

fn main() {
    let mut successes: u32 = 0;

    for _ in 0..100000 {
        if flip_coins() {
            successes += 1;
        }
    }

    println!(
        "A streak of 6 or more appeared in {:.2}% of 100,000 experiments",
        (successes as f64) / 100000 as f64 * 100 as f64
    )
}

fn flip_coins() -> bool {
    let mut coin_flips = vec![];
    let mut rng = rand::thread_rng();

    for _ in 0..100 {
        coin_flips.push(rng.gen_bool(0.5));
    }

    streak_checker(coin_flips)
}

fn streak_checker(coin_flips: Vec<bool>) -> bool {
    let mut streak: u16 = 1;

    for flip in 0..coin_flips.len() - 1 {
        if coin_flips[flip] == coin_flips[flip + 1] {
            streak += 1;
        } else {
            streak = 1;
        }

        if streak == 6 {
            return true;
        }
    }

    return false;
}
