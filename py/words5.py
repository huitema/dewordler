#!/usr/bin/python
# coding=utf-8
#
# This module stores the list of words used in the solver. 

word_list = [
 "aback", "abaft", "abase", "abash", "abate", "abbey", "abbot", "abets",
 "abhor", "abide", "abler", "abode", "abort", "about", "above", "abuse",
 "abuts", "abyss", "ached", "aches", "acids", "acorn", "acres", "acrid",
 "acted", "actor", "acute", "adage", "adapt", "added", "adder", "adept",
 "adieu", "admit", "admix", "adobe", "adopt", "adore", "adorn", "adult",
 "aegis", "affix", "afire", "afoot", "afore", "afoul", "after", "again",
 "agape", "agate", "agent", "agers", "agile", "aging", "aglow", "agony",
 "agree", "ahead", "aided", "aimed", "aimer", "aired", "airer", "aisle",
 "alarm", "album", "alder", "alert", "algae", "alias", "alibi", "alien",
 "align", "alike", "alive", "alkyl", "allay", "alley", "allot", "allow",
 "alloy", "aloes", "aloft", "aloha", "alone", "along", "aloof", "aloud",
 "alpha", "altar", "alter", "amain", "amass", "amaze", "amber", "amble",
 "amend", "amide", "amigo", "amino", "amiss", "amity", "among", "amour",
 "ample", "amply", "amuse", "angel", "anger", "angle", "angry", "angst",
 "anion", "anise", "ankle", "annal", "annex", "annoy", "annul", "annum",
 "anode", "antic", "anvil", "aorta", "apace", "apart", "aphid", "aping",
 "apish", "apple", "apply", "apron", "apsis", "aptly", "arbor", "arced",
 "ardor", "areas", "arena", "argon", "argot", "argue", "arise", "armed",
 "armer", "armor", "aroma", "arose", "array", "arrow", "arson", "ascot",
 "ashen", "ashes", "aside", "asked", "asker", "askew", "aspen", "aspic",
 "assay", "asses", "asset", "aster", "atlas", "atoll", "atoms", "atone",
 "attic", "audio", "audit", "auger", "aught", "augur", "aunts", "aural",
 "auras", "autos", "avail", "avant", "avers", "avert", "avian", "avoid",
 "avows", "await", "awake", "award", "aware", "awash", "awful", "awoke",
 "axers", "axial", "axing", "axiom", "axles", "axons", "azure", "babes",
 "backs", "bacon", "badge", "badly", "bagel", "baggy", "baits", "baked",
 "baker", "bakes", "baler", "bales", "balks", "balky", "balls", "balms",
 "balmy", "balsa", "banal", "bands", "bandy", "bangs", "banjo", "barbs",
 "bards", "bared", "barer", "bares", "barge", "barks", "barns", "baron",
 "basal", "based", "baser", "bases", "basic", "basil", "basin", "basis",
 "baste", "batch", "bathe", "baths", "baton", "bawdy", "bawls", "bayed",
 "bayou", "beach", "beads", "beady", "beaks", "beams", "beans", "beard",
 "bears", "beast", "beats", "beaus", "beech", "beefs", "beefy", "beeps",
 "beers", "beets", "befit", "befog", "began", "beget", "begin", "begot",
 "begun", "beige", "being", "belay", "belch", "belie", "belle", "bells",
 "belly", "below", "belts", "bench", "bends", "beret", "berne", "berry",
 "berth", "beryl", "beset", "bests", "betel", "bevel", "bicep", "biddy",
 "bight", "bigot", "bikes", "bilge", "bilks", "bills", "binds", "binge",
 "bingo", "biota", "biped", "birch", "birds", "birth", "bison", "bitch",
 "biter", "bites", "blabs", "black", "blade", "blame", "bland", "blank",
 "blare", "blase", "blast", "blaze", "bleak", "blear", "bleat", "bleed",
 "blend", "bless", "blimp", "blind", "blink", "blips", "bliss", "blitz",
 "bloat", "blobs", "block", "blocs", "bloke", "blond", "blood", "bloom",
 "blots", "blown", "blows", "bluer", "blues", "bluff", "blunt", "blurb",
 "blurs", "blurt", "blush", "board", "boast", "boats", "bobby", "bodes",
 "bogus", "boils", "bolts", "bombs", "bonds", "boned", "boner", "bones",
 "bonny", "bonus", "booby", "books", "booms", "boors", "boost", "booth",
 "boots", "booty", "booze", "borax", "bored", "borer", "bores", "boric",
 "borne", "boron", "bosom", "bosun", "botch", "bough", "bound", "bouts",
 "bowed", "bowel", "bower", "bowls", "boxed", "boxer", "boxes", "brace",
 "braes", "brags", "braid", "brain", "brake", "brand", "brash", "brass",
 "brats", "brave", "bravo", "brawl", "brawn", "brays", "braze", "bread",
 "break", "breed", "breve", "brews", "briar", "bribe", "brick", "bride",
 "brief", "brier", "brigs", "brine", "bring", "brink", "briny", "brisk",
 "broad", "broil", "broke", "brood", "brook", "broom", "broth", "brown",
 "brows", "brunt", "brush", "brute", "bucks", "buddy", "budge", "buffs",
 "buggy", "bugle", "build", "built", "bulbs", "bulge", "bulks", "bulky",
 "bulls", "bully", "bumps", "bunch", "bunks", "bunny", "bunts", "buoys",
 "burly", "burns", "burnt", "burps", "burrs", "bursa", "burst", "bused",
 "buses", "bushy", "busts", "butte", "butts", "butyl", "buxom", "buyer",
 "buzzy", "bylaw", "bytes", "byway", "cabal", "cabin", "cable", "cache",
 "cacti", "cafes", "caged", "cager", "cages", "cairn", "caked", "cakes",
 "calls", "calms", "calve", "camel", "camps", "canal", "candy", "caner",
 "canny", "canoe", "canon", "canto", "caper", "capes", "cards", "cared",
 "cares", "caret", "cargo", "carol", "carry", "carts", "carve", "cased",
 "cases", "casks", "caste", "casts", "catch", "cater", "caulk", "cause",
 "caved", "caves", "cavil", "cease", "cedar", "ceded", "cells", "cents",
 "chafe", "chaff", "chain", "chair", "chalk", "chant", "chaos", "chaps",
 "charm", "chars", "chart", "chase", "chasm", "cheap", "cheat", "check",
 "cheek", "cheer", "chefs", "chess", "chest", "chews", "chick", "chide",
 "chief", "child", "chili", "chill", "chime", "chink", "chins", "chips",
 "chirp", "chock", "choir", "choke", "chops", "chord", "chore", "chose",
 "chuck", "chunk", "churn", "chute", "cider", "cigar", "cilia", "circa",
 "cited", "cites", "civet", "civic", "civil", "claim", "clamp", "clams",
 "clang", "clank", "claps", "clash", "clasp", "class", "claws", "clays",
 "clean", "clear", "cleft", "clerk", "click", "cliff", "climb", "clime",
 "cling", "clink", "clips", "cloak", "clock", "clods", "clogs", "clone",
 "close", "cloth", "cloud", "clout", "clove", "clown", "clubs", "cluck",
 "clues", "clump", "clung", "coach", "coals", "coast", "coats", "cobra",
 "cocks", "cocky", "cocoa", "coded", "coder", "codes", "coils", "coins",
 "cokes", "colds", "colon", "color", "colts", "combs", "comer", "comes",
 "comet", "comic", "comma", "cones", "conic", "cooks", "cooky", "cools",
 "coons", "coops", "coped", "copes", "copra", "copse", "coral", "cords",
 "cored", "corer", "cores", "corks", "corns", "corny", "corps", "costs",
 "couch", "cough", "could", "count", "court", "cover", "coves", "covet",
 "cowed", "cower", "cowls", "coypu", "crabs", "crack", "craft", "crags",
 "cramp", "crams", "crane", "crank", "crash", "crass", "crate", "crave",
 "crawl", "craze", "crazy", "creak", "cream", "creed", "creek", "creep",
 "crepe", "crept", "crest", "crews", "cribs", "cried", "crier", "cries",
 "crime", "crisp", "croak", "crock", "croft", "crook", "crops", "cross",
 "crowd", "crown", "crows", "crude", "cruel", "crumb", "crush", "crust",
 "crypt", "cubed", "cubes", "cubic", "cuffs", "culls", "culpa", "cults",
 "curbs", "cured", "cures", "curls", "curly", "curry", "curse", "curve",
 "cusps", "cycle", "cynic", "cysts", "daddy", "daily", "dairy", "daisy",
 "dales", "damns", "dance", "dandy", "dared", "darer", "dares", "darns",
 "darts", "dated", "dater", "dates", "datum", "daunt", "dawns", "dazed",
 "deals", "dealt", "deans", "death", "debar", "debit", "debts", "debug",
 "decal", "decay", "decks", "decoy", "deeds", "deems", "deeps", "defer",
 "deify", "deign", "deity", "delay", "dells", "delta", "delve", "demon",
 "demur", "dense", "dents", "depot", "depth", "derby", "desks", "deter",
 "deuce", "devil", "dials", "diary", "dicky", "diets", "digit", "dikes",
 "dildo", "dimes", "dimly", "dined", "diner", "dines", "dingo", "dingy",
 "diode", "dirge", "dirts", "dirty", "discs", "disks", "ditch", "ditto",
 "ditty", "divan", "dived", "diver", "dives", "dizzy", "docks", "dodge",
 "doers", "dogma", "doing", "doled", "doles", "dolls", "dolly", "domed",
 "domes", "donor", "dooms", "doors", "doped", "doper", "dopes", "dosed",
 "doses", "doted", "dotes", "doubt", "dough", "dover", "doves", "dowel",
 "downy", "dowry", "dozed", "dozen", "dozes", "draft", "drags", "drain",
 "drake", "drama", "drank", "drape", "drawl", "drawn", "draws", "dread",
 "dream", "dregs", "dress", "dried", "drier", "dries", "drift", "drill",
 "drily", "drink", "drips", "drive", "droll", "drone", "drool", "droop",
 "drops", "drove", "drown", "drugs", "drums", "drunk", "dryly", "duchy",
 "ducks", "ducts", "duels", "dukes", "dulls", "dully", "dummy", "dumps",
 "dunce", "dunes", "dusky", "dusts", "dusty", "dwarf", "dwell", "dwelt",
 "dyers", "dying", "eager", "eagle", "eared", "earls", "early", "earns",
 "earth", "eased", "easel", "eases", "eaten", "eater", "eaves", "ebony",
 "edged", "edges", "edict", "edits", "eerie", "egged", "eight", "eject",
 "elbow", "elder", "elect", "elegy", "elide", "elite", "elope", "elude",
 "elves", "emacs", "embed", "ember", "emits", "empty", "enact", "ended",
 "ender", "endow", "enema", "enemy", "enjoy", "ennui", "ensue", "enter",
 "entry", "envoy", "epics", "epoch", "equal", "equip", "erase", "erect",
 "erode", "erred", "error", "erupt", "essay", "ether", "ethic", "evade",
 "evens", "event", "every", "evict", "evils", "evoke", "exact", "exalt",
 "exams", "excel", "exert", "exile", "exist", "exits", "expel", "extol",
 "extra", "exult", "eyers", "eying", "fable", "faced", "faces", "facet",
 "facto", "facts", "faded", "fader", "fades", "fails", "faint", "fairs",
 "fairy", "faith", "faked", "faker", "fakes", "falls", "false", "famed",
 "fames", "fancy", "fangs", "farad", "farce", "fared", "fares", "farms",
 "fasts", "fatal", "fated", "fates", "fatty", "fault", "fauna", "favor",
 "fawns", "fears", "feast", "feats", "feeds", "feels", "feign", "felon",
 "felts", "femur", "fence", "ferns", "ferry", "fetal", "fetch", "fetid",
 "fetus", "feuds", "fever", "fewer", "fiber", "field", "fiend", "fiery",
 "fifth", "fifty", "fight", "filed", "filer", "files", "fills", "filly",
 "films", "filth", "final", "finds", "fined", "finer", "fines", "finny",
 "fired", "firer", "fires", "firms", "first", "fishy", "fists", "fitly",
 "fives", "fixed", "fixer", "fixes", "flack", "flags", "flail", "flair",
 "flake", "flaky", "flame", "flank", "flaps", "flare", "flash", "flask",
 "flats", "flaws", "fleas", "flees", "fleet", "flesh", "flick", "flier",
 "flies", "fling", "flint", "flips", "flirt", "float", "flock", "flood",
 "floor", "flops", "flora", "floss", "flour", "flown", "flows", "fluff",
 "fluid", "fluke", "flung", "flush", "flute", "flyer", "foams", "foamy",
 "focal", "focus", "foggy", "foils", "foist", "folds", "folks", "folly",
 "fonts", "foods", "fools", "foray", "force", "fords", "forge", "forks",
 "forms", "forte", "forts", "forty", "forum", "fouls", "found", "fount",
 "fours", "fowls", "foxes", "frail", "frame", "franc", "frank", "fraud",
 "frays", "freak", "freed", "freer", "frees", "freon", "fresh", "friar",
 "fried", "fries", "frill", "frisk", "frock", "frogs", "front", "frost",
 "froth", "frown", "froze", "fruit", "fudge", "fuels", "fugue", "fully",
 "fumed", "fumes", "funds", "fungi", "funny", "furry", "fused", "fuses",
 "fussy", "fuzzy", "gable", "gaily", "gains", "galls", "gamed", "games",
 "gamma", "gangs", "gaped", "gapes", "gases", "gasps", "gassy", "gated",
 "gator", "gaudy", "gauge", "gaunt", "gauze", "gavel", "gawky", "gayer",
 "gayly", "gazed", "gazer", "gazes", "gears", "gecko", "geese", "genes",
 "genie", "genre", "genus", "germs", "ghost", "giant", "giddy", "gifts",
 "gilds", "gills", "girls", "girth", "given", "giver", "gives", "glade",
 "gland", "glare", "glass", "glaze", "gleam", "glean", "glees", "glens",
 "glide", "glint", "gloat", "globe", "gloom", "glory", "gloss", "glove",
 "glows", "glued", "glues", "gnash", "gnats", "gnaws", "gnome", "goals",
 "goats", "godly", "going", "golds", "golly", "goner", "gongs", "goods",
 "goody", "goofs", "goofy", "goose", "gorge", "gouge", "gourd", "gowns",
 "grabs", "grace", "grade", "graft", "grail", "grain", "grams", "grand",
 "grant", "grape", "graph", "grasp", "grass", "grate", "grave", "gravy",
 "graze", "great", "greed", "green", "greet", "grids", "grief", "grill",
 "grime", "grind", "grins", "gripe", "grips", "grist", "grits", "groan",
 "groin", "groom", "grope", "gross", "group", "grove", "growl", "grown",
 "grows", "grubs", "gruff", "grunt", "guano", "guard", "guess", "guest",
 "guide", "guild", "guile", "guilt", "guise", "gulch", "gulfs", "gulls",
 "gully", "gulps", "gunny", "gusto", "gusts", "gusty", "gutsy", "guyed",
 "guyer", "gypsy", "habit", "hacks", "hails", "hairs", "hairy", "haler",
 "halls", "halts", "halve", "hands", "handy", "hangs", "haply", "happy",
 "hardy", "harem", "hares", "harms", "harry", "harsh", "haste", "hasty",
 "hatch", "hated", "hater", "hates", "hauls", "haunt", "haven", "haves",
 "havoc", "hawks", "hazel", "hazes", "heads", "heals", "heaps", "heard",
 "hears", "heart", "heath", "heats", "heave", "heavy", "hedge", "heeds",
 "heels", "hefty", "heirs", "helix", "hello", "hells", "helps", "hence",
 "herbs", "herds", "heres", "heron", "hertz", "hewed", "hewer", "hides",
 "hiked", "hiker", "hikes", "hills", "hilts", "hinge", "hints", "hippo",
 "hired", "hirer", "hires", "hitch", "hoard", "hoary", "hobby", "hoist",
 "holds", "holed", "holes", "holly", "homed", "homer", "homes", "honed",
 "honer", "hones", "honey", "honor", "hoods", "hoofs", "hooks", "hoops",
 "hoots", "hoped", "hopes", "horde", "horns", "horny", "horse", "hoses",
 "hosts", "hotel", "hotly", "hound", "hours", "house", "hovel", "hover",
 "howls", "hulls", "human", "humid", "humor", "hunch", "hunks", "hunts",
 "hurry", "hurts", "husks", "husky", "hutch", "hydra", "hydro", "hyena",
 "hymen", "hymns", "hyper", "icing", "icons", "ideal", "ideas", "idiom",
 "idiot", "idled", "idler", "idles", "idols", "igloo", "image", "impel",
 "imply", "inane", "incur", "index", "inept", "inert", "infer", "infix",
 "infra", "ingot", "inked", "inker", "inlay", "inlet", "inner", "input",
 "inset", "inter", "irate", "irked", "irons", "irony", "isles", "islet",
 "issue", "items", "ivies", "ivory", "jaded", "jails", "jaunt", "jazzy",
 "jeans", "jeeps", "jeers", "jelly", "jenny", "jerks", "jerky", "jests",
 "jewel", "jiffy", "joins", "joint", "joked", "joker", "jokes", "jolly",
 "jolts", "joule", "joust", "judge", "juice", "juicy", "jumbo", "jumps",
 "jumpy", "junks", "junky", "junta", "juror", "kanji", "kappa", "keels",
 "keeps", "keyed", "kicks", "kills", "kinds", "kings", "kinky", "kiosk",
 "kited", "kites", "kitty", "knack", "knave", "knead", "kneed", "kneel",
 "knees", "knell", "knelt", "knife", "knits", "knobs", "knock", "knoll",
 "knots", "known", "knows", "koala", "label", "labor", "laced", "laces",
 "lacks", "laden", "ladle", "lager", "lairs", "lakes", "lambs", "lamed",
 "lames", "lamps", "lance", "lands", "lanes", "lapel", "lapse", "large",
 "larks", "larva", "laser", "lasso", "lasts", "latch", "later", "lathe",
 "laugh", "lawns", "layer", "lazed", "leads", "leafy", "leaks", "leaky",
 "leans", "leaps", "leapt", "learn", "lease", "leash", "least", "leave",
 "ledge", "leech", "leery", "legal", "lemma", "lemon", "lends", "leper",
 "levee", "level", "lever", "liars", "libel", "licks", "liege", "liens",
 "lifer", "lifts", "light", "liked", "liken", "likes", "lilac", "limbo",
 "limbs", "limes", "limit", "limps", "lined", "linen", "liner", "lines",
 "lingo", "links", "lions", "lisps", "lists", "liter", "lithe", "lived",
 "liver", "lives", "livid", "loads", "loans", "loath", "lobby", "lobes",
 "local", "locks", "locus", "lodge", "lofts", "lofty", "logic", "login",
 "loins", "loner", "longs", "looks", "looms", "loops", "loose", "loots",
 "lords", "lorry", "loser", "loses", "lossy", "lotus", "louse", "lousy",
 "loved", "lover", "loves", "lower", "lowly", "loyal", "lucid", "lucks",
 "lucky", "lulls", "lumps", "lumpy", "lunar", "lunch", "lungs", "lurch",
 "lured", "lures", "lurks", "lusts", "lusty", "lutes", "lying", "lymph",
 "lynch", "lyric", "maced", "maces", "macho", "macro", "madam", "madly",
 "magic", "magna", "maids", "mails", "maims", "mains", "maize", "major",
 "maker", "makes", "males", "malts", "mamma", "manes", "mania", "manic",
 "manly", "manor", "maple", "march", "mares", "marry", "marsh", "marts",
 "masks", "mason", "masts", "match", "mated", "mater", "mates", "maxim",
 "maybe", "mayor", "mazes", "meals", "mealy", "means", "meant", "meats",
 "meaty", "medal", "media", "medic", "meets", "melon", "melts", "memos",
 "mends", "menus", "mercy", "merge", "merit", "merry", "meson", "messy",
 "metal", "meted", "meter", "metes", "metro", "mewed", "micro", "midst",
 "might", "milks", "milky", "mimic", "mince", "minds", "mined", "miner",
 "mines", "minis", "minks", "minor", "mints", "minus", "mired", "mires",
 "mirth", "miser", "mists", "misty", "miter", "mixed", "mixer", "mixes",
 "mixup", "moans", "moats", "mocks", "modal", "model", "modem", "modes",
 "modus", "moist", "molar", "molds", "moles", "mommy", "money", "monks",
 "month", "moods", "moody", "moons", "moose", "moped", "moral", "mores",
 "moron", "mossy", "motel", "motif", "motor", "motto", "mould", "mound",
 "mount", "mourn", "mouse", "mousy", "mouth", "moved", "mover", "moves",
 "movie", "mowed", "mower", "mucus", "muddy", "muffs", "mules", "multi",
 "mummy", "munch", "mural", "murky", "mused", "muses", "mushy", "music",
 "musks", "musts", "musty", "muted", "nabla", "nadir", "nails", "naive",
 "naked", "named", "namer", "names", "nasal", "nasty", "natal", "naval",
 "navel", "nears", "necks", "needs", "needy", "neigh", "nerve", "nests",
 "never", "newer", "newly", "nicer", "niche", "nicks", "niece", "nifty",
 "night", "nines", "ninth", "nitty", "noble", "nobly", "nodal", "nodes",
 "noise", "noisy", "nonce", "nooks", "noons", "noose", "norms", "north",
 "nosed", "noses", "notch", "noted", "notes", "nouns", "novel", "nudge",
 "nulls", "numbs", "nurse", "nylon", "nymph", "oaken", "oases", "oasis",
 "oaten", "oaths", "obese", "obeys", "occur", "ocean", "octal", "octet",
 "odder", "oddly", "odium", "odors", "offer", "often", "oiled", "oiler",
 "olden", "older", "olive", "omega", "omens", "omits", "onion", "onset",
 "oozed", "opals", "opens", "opera", "opium", "opted", "optic", "orbit",
 "order", "organ", "other", "otter", "ought", "ounce", "outdo", "outer",
 "ovals", "ovary", "ovens", "overt", "owing", "owned", "owner", "oxide",
 "ozone", "paced", "pacer", "paces", "packs", "pacts", "paddy", "pagan",
 "paged", "pager", "pages", "pails", "pains", "paint", "pairs", "paled",
 "paler", "pales", "palms", "palsy", "panda", "panel", "panes", "pangs",
 "panic", "pansy", "pants", "panty", "papal", "paper", "parch", "pares",
 "parry", "parse", "parts", "party", "passe", "paste", "pasts", "patch",
 "paten", "paths", "patio", "patty", "pause", "paved", "paves", "pawns",
 "payed", "payer", "peace", "peach", "peaks", "peals", "pearl", "pears",
 "pecks", "pedal", "peeks", "peels", "peeps", "peers", "pelts", "penal",
 "pence", "pends", "penis", "penny", "peony", "peppy", "perch", "peril",
 "perky", "pests", "petal", "petri", "petty", "phase", "phone", "phony",
 "photo", "phyla", "piano", "picas", "picks", "picky", "piece", "piers",
 "piety", "piggy", "piker", "pikes", "piled", "piles", "pills", "pilot",
 "pinch", "pined", "pines", "pinks", "pinto", "pints", "pious", "piped",
 "pipes", "pique", "pitch", "pithy", "pivot", "pixel", "pizza", "place",
 "plaid", "plain", "plait", "plane", "plank", "plans", "plant", "plate",
 "plays", "plaza", "plead", "pleas", "pleat", "plied", "plies", "plots",
 "plows", "ploys", "pluck", "plugs", "plumb", "plume", "plump", "plums",
 "plunk", "plush", "poach", "podia", "poems", "poets", "point", "poise",
 "poked", "poker", "pokes", "polar", "poled", "poles", "polio", "polka",
 "polls", "ponds", "pooch", "pools", "poppy", "porch", "pored", "pores",
 "ports", "posed", "poser", "poses", "posit", "posse", "posts", "pouch",
 "pound", "pours", "pouts", "power", "prank", "prate", "preen", "press",
 "preys", "price", "prick", "pride", "prima", "prime", "print", "prior",
 "prism", "privy", "prize", "probe", "prone", "prong", "proof", "props",
 "prose", "proud", "prove", "prowl", "prows", "proxy", "prune", "psalm",
 "psych", "puffs", "pulls", "pulse", "pumps", "punch", "punts", "pupil",
 "puppy", "purer", "purge", "purrs", "purse", "pussy", "putty", "pygmy",
 "quack", "quaff", "quail", "quake", "qualm", "quark", "quart", "quash",
 "quasi", "queen", "queer", "quell", "query", "quest", "queue", "quick",
 "quiet", "quill", "quilt", "quint", "quirk", "quite", "quits", "quota",
 "quote", "quoth", "rabbi", "rabid", "raced", "racer", "races", "racks",
 "radar", "radii", "radio", "radix", "radon", "rafts", "raged", "rages",
 "raids", "rails", "rains", "rainy", "raise", "raked", "rakes", "rally",
 "ramps", "ranch", "randy", "range", "rangy", "ranks", "rants", "raped",
 "raper", "rapes", "rapid", "rarer", "rasps", "rated", "rater", "rates",
 "ratio", "raved", "raven", "raves", "rawer", "rawly", "razor", "reach",
 "react", "reads", "ready", "realm", "reals", "reaps", "rears", "rebel",
 "recta", "recur", "redly", "reeds", "reefs", "reels", "refer", "regal",
 "reign", "reins", "relax", "relay", "relic", "remit", "renal", "rends",
 "renew", "rents", "repay", "repel", "reply", "rerun", "reset", "resin",
 "rests", "retch", "retry", "reuse", "revel", "rhino", "rhyme", "rider",
 "rides", "ridge", "rifle", "right", "rigid", "rigor", "rinds", "rings",
 "rinse", "riots", "ripen", "risen", "riser", "rises", "risks", "risky",
 "rites", "rival", "river", "rivet", "roach", "roads", "roams", "roars",
 "roast", "robed", "robes", "robin", "robot", "rocks", "rocky", "rodeo",
 "rogue", "roles", "rolls", "romps", "roofs", "rooms", "roomy", "roost",
 "roots", "roped", "roper", "ropes", "roses", "rotor", "rouge", "rough",
 "round", "rouse", "route", "roved", "rover", "roves", "rowdy", "rowed",
 "rower", "royal", "ruble", "ruddy", "ruins", "ruled", "ruler", "rules",
 "rumen", "rummy", "rumor", "rungs", "rupee", "rural", "rusts", "rusty",
 "saber", "sable", "sacks", "sadly", "safer", "safes", "sages", "sails",
 "saint", "sakes", "salad", "sales", "salon", "salts", "salty", "salve",
 "sands", "sandy", "saner", "sated", "sates", "satin", "satyr", "sauce",
 "saucy", "saved", "saver", "saves", "savor", "sawed", "sayer", "scald",
 "scale", "scalp", "scaly", "scans", "scant", "scare", "scarf", "scars",
 "scary", "scene", "scent", "scoff", "scold", "scoop", "scoot", "scope",
 "score", "scorn", "scour", "scout", "scowl", "scram", "scrap", "screw",
 "scrub", "scuba", "seals", "sealy", "seams", "seamy", "seats", "sects",
 "sedan", "sedge", "seeds", "seedy", "seeks", "seems", "seeps", "seers",
 "seize", "sells", "sends", "sense", "sepia", "serfs", "serif", "serum",
 "serve", "servo", "setup", "seven", "sever", "sewed", "sewer", "sexed",
 "sexes", "shack", "shade", "shady", "shaft", "shake", "shaky", "shale",
 "shall", "shame", "shams", "shape", "shard", "share", "shark", "sharp",
 "shave", "shawl", "sheaf", "shear", "sheds", "sheen", "sheep", "sheer",
 "sheet", "sheik", "shelf", "shell", "shied", "shies", "shift", "shill",
 "shine", "shiny", "ships", "shire", "shirk", "shirt", "shoal", "shock",
 "shoed", "shoes", "shone", "shook", "shoot", "shops", "shore", "shorn",
 "short", "shots", "shout", "shove", "shown", "shows", "showy", "shred",
 "shrew", "shrub", "shrug", "shuns", "shunt", "shuts", "shyly", "sided",
 "sides", "siege", "sieve", "sighs", "sight", "sigma", "signs", "silks",
 "silky", "sills", "silly", "silts", "since", "sines", "sinew", "singe",
 "sings", "sinks", "sinus", "sired", "siren", "sires", "sirup", "sited",
 "sites", "sixes", "sixth", "sixty", "sized", "sizes", "skate", "skews",
 "skied", "skies", "skiff", "skill", "skimp", "skims", "skins", "skips",
 "skirt", "skulk", "skull", "skunk", "slack", "slain", "slams", "slang",
 "slant", "slaps", "slash", "slate", "slats", "slave", "slays", "sleds",
 "sleek", "sleep", "sleet", "slept", "slice", "slick", "slide", "slime",
 "slimy", "sling", "slips", "slits", "sloop", "slope", "slops", "sloth",
 "slots", "slows", "slugs", "slump", "slums", "slung", "slurp", "slurs",
 "slyly", "smack", "small", "smart", "smash", "smear", "smell", "smelt",
 "smile", "smirk", "smite", "smith", "smock", "smoke", "smoky", "smote",
 "snack", "snafu", "snail", "snake", "snaps", "snare", "snark", "snarl",
 "sneak", "sneer", "sniff", "snipe", "snoop", "snore", "snort", "snout",
 "snows", "snowy", "snuff", "soaks", "soaps", "soapy", "soars", "sober",
 "socks", "sofas", "soggy", "soils", "solar", "soles", "solid", "solos",
 "solve", "sonar", "songs", "sonic", "sonny", "sooth", "sorer", "sores",
 "sorry", "sorts", "souls", "sound", "soups", "sours", "south", "space",
 "spank", "spans", "spare", "spark", "spasm", "spate", "spawn", "speak",
 "spear", "speck", "speed", "spell", "spend", "spent", "sperm", "spice",
 "spicy", "spies", "spike", "spill", "spilt", "spine", "spins", "spiny",
 "spire", "spite", "spits", "split", "spoil", "spoke", "spoof", "spook",
 "spool", "spoon", "spore", "sport", "spots", "spout", "spray", "spree",
 "sprig", "spunk", "spurn", "spurs", "spurt", "squad", "squat", "squaw",
 "squid", "stabs", "stack", "staff", "stage", "stags", "staid", "stain",
 "stair", "stake", "stale", "stalk", "stall", "stamp", "stand", "stare",
 "stark", "stars", "start", "state", "stave", "stays", "stead", "steak",
 "steal", "steam", "steed", "steel", "steep", "steer", "stems", "steps",
 "stern", "stews", "stick", "stiff", "stile", "still", "stilt", "sting",
 "stink", "stint", "stirs", "stock", "stoke", "stole", "stomp", "stony",
 "stood", "stool", "stoop", "stops", "store", "stork", "storm", "story",
 "stout", "stove", "strap", "straw", "stray", "strew", "strip", "strut",
 "stubs", "stuck", "studs", "study", "stuff", "stump", "stung", "stunt",
 "style", "styli", "suave", "sucks", "sugar", "suing", "suite", "suits",
 "sulfa", "sulks", "sulky", "sumac", "sunny", "super", "surge", "surly",
 "swain", "swami", "swamp", "swank", "swans", "swaps", "swarm", "swear",
 "sweat", "sweep", "sweet", "swell", "swept", "swift", "swims", "swine",
 "swing", "swipe", "swirl", "swish", "swiss", "swoon", "swoop", "sword",
 "swore", "sworn", "swung", "synod", "syrup", "table", "taboo", "tacit",
 "tails", "taint", "taken", "taker", "takes", "tales", "talks", "tally",
 "tamed", "tamer", "tames", "tangy", "tanks", "taped", "taper", "tapes",
 "tardy", "tarry", "tasks", "taste", "taunt", "tawny", "taxed", "taxes",
 "taxis", "teach", "teams", "tears", "tease", "teems", "teens", "teeth",
 "tells", "tempt", "tends", "tenor", "tense", "tenth", "tents", "terms",
 "tests", "texts", "thank", "thats", "thaws", "theft", "their", "theme",
 "there", "these", "thick", "thief", "thigh", "thing", "think", "third",
 "thong", "thorn", "those", "three", "threw", "throb", "throw", "thuds",
 "thugs", "thumb", "thump", "ticks", "tidal", "tided", "tides", "tiers",
 "tiger", "tight", "tilde", "tiled", "tiles", "tills", "tilts", "timed",
 "timer", "times", "timid", "tinge", "tinny", "tints", "tired", "tires",
 "tithe", "title", "toads", "toast", "today", "toils", "token", "tolls",
 "tombs", "toned", "toner", "tones", "tongs", "tonic", "tools", "tooth",
 "toper", "topic", "torch", "torus", "total", "touch", "tough", "tours",
 "towed", "towel", "tower", "towns", "toyed", "trace", "track", "tract",
 "trade", "trail", "train", "trait", "tramp", "traps", "trash", "trays",
 "tread", "treat", "trees", "treks", "trend", "tress", "trial", "tribe",
 "trick", "tried", "trier", "tries", "trill", "trims", "trips", "troll",
 "troop", "trots", "trout", "truce", "truck", "trued", "truer", "trues",
 "truly", "trump", "trunk", "trust", "truth", "tuber", "tubes", "tucks",
 "tufts", "tulip", "tumor", "tuned", "tuner", "tunes", "tunic", "tuple",
 "turns", "tutor", "twain", "twang", "tweed", "twice", "twigs", "twill",
 "twine", "twins", "twirl", "twist", "tying", "typed", "types", "ulcer",
 "ultra", "unary", "uncle", "under", "undid", "undue", "unfit", "unify",
 "union", "unite", "units", "unity", "untie", "until", "upper", "upset",
 "urban", "urged", "urges", "urine", "usage", "users", "usher", "using",
 "usual", "usurp", "utter", "vacuo", "vague", "vales", "valet", "valid",
 "valor", "value", "valve", "vanes", "vapor", "vases", "vault", "vaunt",
 "veers", "veils", "veins", "venom", "vents", "verbs", "verge", "versa",
 "verse", "vests", "vexed", "vexes", "vials", "vices", "video", "views",
 "vigor", "villa", "vines", "viper", "virus", "visas", "visit", "visor",
 "vista", "vitae", "vital", "vivid", "vocal", "vogue", "voice", "voids",
 "volts", "vomit", "voted", "voter", "votes", "vouch", "vowed", "vowel",
 "vower", "wacky", "waded", "wader", "wades", "wafer", "waged", "wager",
 "wages", "wagon", "wails", "waist", "waits", "waive", "waked", "waken",
 "wakes", "wales", "walks", "waltz", "waned", "wanes", "wanly", "wants",
 "wards", "wares", "warms", "warns", "warps", "warts", "wasps", "waste",
 "watch", "water", "waved", "waver", "waves", "waxed", "waxen", "waxer",
 "waxes", "wears", "weary", "weave", "wedge", "weeds", "weeps", "weigh",
 "weird", "welds", "welsh", "wench", "wetly", "whack", "whale", "wharf",
 "wheat", "wheel", "whelp", "where", "which", "while", "whims", "whine",
 "whips", "whirl", "whirr", "whisk", "white", "whole", "whoop", "whore",
 "whorl", "whose", "wicks", "widen", "wider", "widow", "width", "wield",
 "wiles", "wilts", "wince", "winds", "windy", "wined", "winer", "wines",
 "wings", "winks", "wiped", "wiper", "wipes", "wired", "wires", "wised",
 "wiser", "wisps", "witch", "witty", "wives", "woman", "wombs", "women",
 "woody", "wooed", "wooer", "woofs", "wools", "words", "wordy", "works",
 "world", "worms", "worry", "worse", "worst", "worth", "would", "wound",
 "woven", "wraps", "wrath", "wreak", "wreck", "wrens", "wrest", "wring",
 "wrist", "write", "writs", "wrong", "wrote", "wrung", "yanks", "yards",
 "yarns", "yearn", "years", "yeast", "yelps", "yield", "yokes", "young",
 "yours", "youth", "zebra", "zeros", "zonal", "zoned", "zones", "zooms" ]
