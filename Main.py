import discord 
from  discord.ext import commands
import json 
Async = commands.Bot(command_prefix="$",intents=discord.Intents.all())

token ="#Enter your token here "
#Read Readme.md
def get_noprefix_users():
    try:
        with open('noprefixsanemi.json', 'r') as file:
            noprefix_users = json.load(file)
            if not isinstance(noprefix_users, list):
                noprefix_users = []
    except (FileNotFoundError, json.JSONDecodeError):
        noprefix_users = []
    return noprefix_users

def update_noprefix_users(noprefix_users):
    with open('noprefixsanemi.json', 'w') as file:
        json.dump(noprefix_users, file, indent=4)

@Async.event
async def on_message(message):
    
    if message.author == Async.user:
        return

    noprefix_users = get_noprefix_users()
         
    if str(message.author.id) in noprefix_users:  

        ctx = await Async.get_context(message)
        if ctx.valid: 


            await Async.invoke(ctx)   

        return   
    await Async.process_commands(message)


async def ghosty_prefix(bot, message):
    noprefix_users = get_noprefix_users()
    if str(message.author.id) in noprefix_users:
        return ['!', '']  
    return '!'  

Async.command_prefix = ghosty_prefix 

@Async.command(aliases=["Noprefix", "Np"])
async def noprefix(ctx):
    ghosty_allowed = ['978271662464176179', '1076807315883302922']  

    try:
        if str(ctx.author.id) not in ghosty_allowed:
            not_authorized_ghosty = discord.Embed(
                title="",
                description="<a:MekoCross:1219168257072955454> You are not authorized to use this command.",
                color=0x2a2d30
            )
            await ctx.send(embed=not_authorized_ghosty)
            return
        usage_ghosty = discord.Embed(
            title="",
            description="<:XcapeInfo:1219891694049296414> Usage: !noprefix_add @user OR !noprefix_remove @user",
            color=0x2a2d30
        )
        await ctx.send(embed=usage_ghosty)
    except Exception as e:
        print(f"Error in noprefix command: {e}")
        await ctx.send("An error occurred while processing the noprefix command.")

@Async.command(aliases=["Noprefix_add", "Np_add", "np_add"])
async def noprefix_add(ctx, user: discord.Member):
    ghosty_allowed = ['978271662464176179', '1076807315883302922']  

    try:
        if str(ctx.author.id) not in ghosty_allowed:
            not_authorized_ghosty = discord.Embed(
                title="",
                description="<a:MekoCross:1219168257072955454> You are not authorized to use this command.",
                color=0x2a2d30
            )
            await ctx.send(embed=not_authorized_ghosty)
            return

        noprefix_users = get_noprefix_users()
        if str(user.id) not in noprefix_users:
            noprefix_users.append(str(user.id))
            update_noprefix_users(noprefix_users)
            added_np_ghosty = discord.Embed(
                title="",
                description=f"<a:MekoCheck:1219171161120833617> {user.mention} can now use all commands without a prefix.",
                color=0x2a2d30
            )
            await ctx.send(embed=added_np_ghosty)
        else:
            already_np_ghosty = discord.Embed(
                title="",
                description=f"<a:MekoCross:1219168257072955454> {user.mention} is already allowed to use all commands without a prefix.",
                color=0x2a2d30
            )
            await ctx.send(embed=already_np_ghosty)
    except Exception as e:
        print(f"Error in noprefix_add command: {e}")
        await ctx.send("An error occurred while adding the user to the noprefix list.")

@Async.command(aliases=["Noprefix_remove", "Np_remove", "np_remove"])
async def noprefix_remove(ctx, user: discord.Member):
    ghosty_allowed = ['978271662464176179', '1076807315883302922']  

    try:
        if str(ctx.author.id) not in ghosty_allowed:
            not_authorized_ghosty = discord.Embed(
                title="",
                description="<a:MekoCross:1219168257072955454> You are not authorized to use this command.",
                color=0x2a2d30
            )
            await ctx.send(embed=not_authorized_ghosty)
            return

        noprefix_users = get_noprefix_users()
        if str(user.id) in noprefix_users:
            noprefix_users.remove(str(user.id))
            update_noprefix_users(noprefix_users)
            removed_np_ghosty = discord.Embed(
                title="",
                description=f"<a:MekoCheck:1219171161120833617> {user.mention} is no longer allowed to use all commands without a prefix.",
                color=0x2a2d30
            )
            await ctx.send(embed=removed_np_ghosty)
        else:
            not_in_np_ghosty = discord.Embed(
                title="",
                description=f"<a:MekoCross:1219168257072955454> {user.mention} is not in the list of users allowed to use all commands without a prefix.",
                color=0x2a2d30
            )
            await ctx.send(embed=not_in_np_ghosty)
    except Exception as e:
        print(f"Error in noprefix_remove command: {e}")
        await ctx.send("An error occurred while removing the user from the noprefix list.")
Async.run("token")
