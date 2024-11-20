import random
from datetime import datetime, timedelta

# Expanded list of unique player nicknames
players = [
    'ShadowHunter', 'LunaWolf', 'DragonSlayer', 'PixelMaster', 'KnightRider', 'MysticMiner',
    'SkyBreaker', 'ThunderBolt', 'FireFury', 'AquaMarine', 'EarthShaker', 'WindWhisper',
    'StarGazer', 'IronHeart', 'GhostWalker', 'BladeRunner', 'CyberNinja', 'QuantumLeap',
    'NovaStar', 'CrystalMage', 'ArcaneArcher', 'SilentStorm', 'RogueAgent', 'EchoEcho',
    'VortexVoid', 'SolarFlare', 'GravityShift', 'NeonGlow', 'StealthSniper', 'FrostBite',
    'StormChaser', 'ElectricPulse', 'MinerJoe', 'BuilderBob', 'ExplorerEve', 'CrafterCarl',
    'DiggerDan', 'LumberJack', 'FarmerFred', 'HunterHelen', 'WizardWill', 'KnightKevin',
    'ArcherAmy', 'NinjaNick', 'PiratePete', 'ZombieZack', 'MaliciousPlayer'  # Keep MaliciousPlayer for your manual addition
]

online_players = set()

# Expanded actions with more miscellaneous events
actions = [
    '{} joined the game',
    '{} left the game',
    '<{}> {}',
    '[Essentials] {} issued server command: {}',
    '[WorldEdit] {} used {}',
    '[AuthMe] {} logged in',
    '{} was slain by {}',
    '{} earned the achievement [{}]',
    '{} changed their skin',
    '[Server] Announcement: {}',
    'Weather changed to {}',
    'Time set to {}',
    '{} picked up {}',
    '{} placed {} at {}',
    '{} broke {} at {}',
    '{} was kicked from the game',
    '{} was banned from the game',
    '[LagMonitor] Server TPS dropped to {}',
    '[ERROR] Could not pass event {} to {}',
    'Saving chunks for level \'world\'/Overworld',
    'Preparing spawn area: {}%',
    '{} traded {} with a Villager',
    '{} tamed a {}',
    '{} completed challenge [{}]',
    '{} died from {}',
    '{} enchanted {} with {}',
    '[AntiCheat] {} was flagged for {}',
    '[Vote] {} voted for the server and received {}',
    '[Backup] World backup completed successfully',
    '{} set home at {}',
    '[Achievements] {} has unlocked all achievements!',
    '[McMMO] {} activated skill {}',
    '[Factions] {} claimed land for faction {}',
    '[Server] {} reached level {}',
]

# Additional sample data for new events
chat_messages = [
    'Hello!', 'Anyone wants to mine?', 'Looking for diamonds!', 'Let\'s build a house.',
    'Watch out for creepers!', 'Anyone up for a raid?', 'Check out my new skin!',
    'I found a village!', 'Let\'s go to the Nether.', 'Who needs iron?', 'Selling emeralds!',
    'Does anyone have blaze rods?', 'I need help with this quest.', 'Join my faction!',
    'Can someone help me?', 'This server is awesome!', 'What plugins are installed?',
    'Be careful in the End.', 'I lost all my items!', 'How do I set a home?'
]

commands = [
    '/tp {}', '/give {} diamond 64', '/sethome', '/warp spawn', '/time set day', '/weather clear',
    '/gamemode creative', '/fly', '/msg {}', '/ban {}', '/kick {}', '/mute {}', '/unmute {}',
    '/god', '/heal', '/back', '/home', '/sell hand', '/balance'
]

worldedit_commands = ['//wand', '//set stone', '//copy', '//paste', '//undo', '//redo', '//replace', '//sphere']

achievements = [
    'Getting Wood', 'Time to Mine!', 'Hot Topic', 'Acquire Hardware', 'Monster Hunter',
    'Diamonds!', 'Enchanter', 'Overkill', 'Librarian', 'The End?', 'The End.', 'Beaconator',
    'Adventuring Time', 'Overpowered'
]

challenges = [
    'Defeat the Ender Dragon', 'Collect all music discs', 'Explore all biomes',
    'Craft a Netherite Sword', 'Complete the Beacon', 'Tame all cat variants',
    'Breed all animals', 'Trade with a Villager at max level'
]

announcements = [
    'Server maintenance at midnight.', 'Double XP weekend starts now!', 'Welcome new players!',
    'Check out our new Discord server!', 'Vote for us to get rewards!', 'New plugin added: McMMO',
    'Happy hour! Earn double rewards for the next hour.', 'Event starting in 10 minutes!'
]

weathers = ['clear', 'rain', 'thunder']
items = [
    'diamond', 'iron_ingot', 'gold_ingot', 'emerald', 'redstone', 'lapis_lazuli', 'netherite_ingot',
    'ender_pearl', 'blaze_rod', 'shulker_shell'
]
blocks = [
    'stone', 'dirt', 'grass_block', 'oak_log', 'cobblestone', 'obsidian', 'netherrack',
    'sand', 'gravel', 'soul_sand'
]
entities = [
    'Zombie', 'Skeleton', 'Creeper', 'Spider', 'Enderman', 'Blaze', 'Wither Skeleton',
    'Slime', 'Ghast', 'Silverfish'
]
locations = [
    '(100, 64, 200)', '(-50, 70, 300)', '(0, 64, 0)', '(200, 70, -100)', '(-150, 65, 150)',
    '(256, 72, -256)', '(64, 64, 64)', '(-128, 70, 128)', '(512, 80, 512)', '(-300, 60, -300)'
]
errors = ['PlayerInteractEvent', 'BlockBreakEvent', 'EntityDeathEvent', 'InventoryClickEvent', 'ChatEvent']
plugins = ['Essentials', 'WorldEdit', 'AuthMe', 'LagMonitor', 'McMMO', 'WorldGuard', 'DynMap', 'AntiCheat', 'Vault', 'LuckPerms']
tames = ['Wolf', 'Cat', 'Horse', 'Parrot', 'Donkey', 'Llama', 'Fox']
skills = ['Super Breaker', 'Giga Drill Breaker', 'Tree Feller', 'Serrated Strikes', 'Skull Splitter']
factions = ['Knights', 'Mages', 'Hunters', 'Explorers', 'Builders']

start_time = datetime.now() - timedelta(hours=5)
current_time = start_time

# Number of log entries to generate
num_entries = 10000000  # 10 million entries

# Open the log file for writing
with open('server.log', 'w') as log_file:
    for i in range(num_entries):
        # Increment current time by 1 to 3 seconds
        current_time += timedelta(seconds=random.randint(1, 3))
        time_str = current_time.strftime('%H:%M:%S')
        
        # Randomly select an action
        action_template = random.choice(actions)
        player = random.choice(players)
        action = ''
        
        # Handle different action templates
        if action_template == '{} joined the game':
            if player not in online_players:
                online_players.add(player)
                action = action_template.format(player)
            else:
                continue  # Player is already online, skip
        elif action_template == '{} left the game':
            if player in online_players:
                online_players.remove(player)
                action = action_template.format(player)
            else:
                continue  # Player is not online, skip
        elif action_template == '<{}> {}':
            if player in online_players:
                message = random.choice(chat_messages)
                action = action_template.format(player, message)
            else:
                continue  # Player is not online, skip
        elif action_template == '[Essentials] {} issued server command: {}':
            if player in online_players:
                command = random.choice(commands)
                if '{}' in command:
                    target_player = random.choice(players)
                    command = command.format(target_player)
                action = action_template.format(player, command)
            else:
                continue
        elif action_template == '[WorldEdit] {} used {}':
            if player in online_players:
                command = random.choice(worldedit_commands)
                action = action_template.format(player, command)
            else:
                continue
        elif action_template == '[AuthMe] {} logged in':
            action = action_template.format(player)
        elif action_template == '{} was slain by {}':
            if player in online_players:
                possible_entities = entities + list(online_players - {player})
                entity = random.choice(possible_entities)
                action = action_template.format(player, entity)
            else:
                continue
        elif action_template == '{} earned the achievement [{}]':
            if player in online_players:
                achievement = random.choice(achievements)
                action = action_template.format(player, achievement)
            else:
                continue
        elif action_template == '{} changed their skin':
            if player in online_players:
                action = action_template.format(player)
            else:
                continue
        elif action_template == '[Server] Announcement: {}':
            announcement = random.choice(announcements)
            action = action_template.format(announcement)
        elif action_template == 'Weather changed to {}':
            weather = random.choice(weathers)
            action = action_template.format(weather)
        elif action_template == 'Time set to {}':
            time_set = random.choice(['day', 'night', 'noon', 'midnight'])
            action = action_template.format(time_set)
        elif action_template == '{} picked up {}':
            if player in online_players:
                item = random.choice(items)
                action = action_template.format(player, item)
            else:
                continue
        elif action_template == '{} placed {} at {}':
            if player in online_players:
                block = random.choice(blocks)
                location = random.choice(locations)
                action = action_template.format(player, block, location)
            else:
                continue
        elif action_template == '{} broke {} at {}':
            if player in online_players:
                block = random.choice(blocks)
                location = random.choice(locations)
                action = action_template.format(player, block, location)
            else:
                continue
        elif action_template == '{} was kicked from the game':
            if player in online_players:
                online_players.remove(player)
                action = action_template.format(player)
            else:
                continue
        elif action_template == '{} was banned from the game':
            if player in online_players:
                online_players.remove(player)
                action = action_template.format(player)
            else:
                continue
        elif action_template == '[LagMonitor] Server TPS dropped to {}':
            tps = round(random.uniform(5.0, 19.9), 1)
            action = action_template.format(tps)
        elif action_template == '[ERROR] Could not pass event {} to {}':
            event = random.choice(errors)
            plugin = random.choice(plugins)
            action = action_template.format(event, plugin)
        elif action_template == 'Saving chunks for level \'world\'/Overworld':
            action = action_template
        elif action_template == 'Preparing spawn area: {}%':
            percent = random.randint(0, 100)
            action = action_template.format(percent)
        elif action_template == '{} traded {} with a Villager':
            if player in online_players:
                item = random.choice(items)
                action = action_template.format(player, item)
            else:
                continue
        elif action_template == '{} tamed a {}':
            if player in online_players:
                animal = random.choice(tames)
                action = action_template.format(player, animal)
            else:
                continue
        elif action_template == '{} completed challenge [{}]':
            if player in online_players:
                challenge = random.choice(challenges)
                action = action_template.format(player, challenge)
            else:
                continue
        elif action_template == '{} died from {}':
            if player in online_players:
                cause = random.choice(['fall damage', 'lava', 'drowning', 'fire', 'explosion', 'magic'])
                action = action_template.format(player, cause)
            else:
                continue
        elif action_template == '{} enchanted {} with {}':
            if player in online_players:
                item = random.choice(items)
                enchantment = random.choice(['Sharpness V', 'Efficiency IV', 'Unbreaking III', 'Fortune II'])
                action = action_template.format(player, item, enchantment)
            else:
                continue
        elif action_template == '[AntiCheat] {} was flagged for {}':
            if player in online_players:
                cheat = random.choice(['Fly hacking', 'Speed hacking', 'X-Ray'])
                action = action_template.format(player, cheat)
            else:
                continue
        elif action_template == '[Vote] {} voted for the server and received {}':
            if player in online_players:
                reward = random.choice(['Vote Key', f'{random.randint(1,64)} {random.choice(items)}'])
                action = action_template.format(player, reward)
            else:
                continue
        elif action_template == '[Backup] World backup completed successfully':
            action = action_template
        elif action_template == '{} set home at {}':
            if player in online_players:
                location = random.choice(locations)
                action = action_template.format(player, location)
            else:
                continue
        elif action_template == '[Achievements] {} has unlocked all achievements!':
            if player in online_players:
                action = action_template.format(player)
            else:
                continue
        elif action_template == '[McMMO] {} activated skill {}':
            if player in online_players:
                skill = random.choice(skills)
                action = action_template.format(player, skill)
            else:
                continue
        elif action_template == '[Factions] {} claimed land for faction {}':
            if player in online_players:
                faction = random.choice(factions)
                action = action_template.format(player, faction)
            else:
                continue
        elif action_template == '[Server] {} reached level {}':
            if player in online_players:
                level = random.randint(2, 100)
                action = action_template.format(player, level)
            else:
                continue
        else:
            continue  # Skip unknown templates
        
        # Create the log entry
        log_entry = f'[{time_str}] [Server thread/INFO]: {action}'
        log_file.write(log_entry + '\n')
        
        # Ensure at least one player is online
        if not online_players:
            player_to_join = random.choice(players)
            online_players.add(player_to_join)
            join_entry = f'[{time_str}] [Server thread/INFO]: {player_to_join} joined the game'
            log_file.write(join_entry + '\n')
        
        # Periodically add server status messages
        if i % 500000 == 0 and i != 0:
            status_entry = f'[{time_str}] [Server thread/INFO]: [Server] Current online players: {len(online_players)}'
            log_file.write(status_entry + '\n')

