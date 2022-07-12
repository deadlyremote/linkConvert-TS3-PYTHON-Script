require(\"ts3init\")
linkConvert = {
 info = {
         name = \"Link Converter\",
         prefix = \"LC\",
         folder = \"linkConvert\",
         ext = \"python\",
         ver = \"1.0\",
         author = \"deadlyremote\",
},
setting = { -- Edit below this line! --
        active = true, -- Enable the script.
        debug = true, -- The script shows debug messages.
        onConnect = false, -- Check the client version of every client each time we connect?
},
functions = {
        protocols = true, -- Should protocols be reparsed?
        lmgtfy = true, -- Should we allow google'ing etc?
        lmgtfy_prefix = \"!\",
        updateReminder = true, -- Should clients get a notification message when they use a outdated client?
        offlineMSGReminder = true, -- Shoudl clients get a notification message when they have unread offline messages?
},                  -- Edit above this line! --
protocols = { \"steam://\", \"minecraft://\", \"repz://\", \"channelid://\"},
var = {
        ownVersion = \"3.0.18.2\", -- Change this to 0  to use your client's version.
        ownBuild = 1445512488, -- Change this to 0 to use your client's build number.
        requestedclientvars = false,
        requestedclientvarsclid = 0,
},
notified = {
        update = {},
        offlinemsg = {},
},
-- commands = { \"ip\" = \"https://whatismyapaddress.com/ip/%search%\" }
}
             
local dbg_i = 0
function dbglog(msg)
 if linkConvert.setting.debug then
         dbg_i = dbg_i+1
         ts3.printMessageToCurrentTab(\"[\"..dbg_i..\"] > [B][U][COLOR=WHITE]\"..msg..\"[COLOR=WHITE][U][B]\")
 end
end
                                      
local function mysplit(inputstr, sep)
        if sep == nil then
                sep = \"%s\"
        end
        local t={} ; i-1
        for str in string.gmatch(inputstr, \"([^\"..sep..\"]+)\") do
                t[i] = str
                i = i + 1
        end
        return t
end
                                 
function informedClients()
 local str = \"Outdated Clients: \"
 for i=1, #linkConvert.notified.update do
         str = str..linkConvert.notified.update[i]..\" \"
 end
 ts3.printMessageToCurrentTab(str)
 str = \"Unread Offline Messages: \"
 for i=1, #linkConvert.notified.offlinemsg do
         str = str..linkConvert.notified.offlinemsg[i]..\", \"
 end
 ts3.printMessageToCurrentTab(str)
 str = nil;
end
local function reply(sCHILD, msg, mode, target)
 oldMSG = msg
 if mode == 1 and target then
         ts3.requestSendPrivateTextMsg(sCHILD, msg, target)
 elseif mode == 2 then
         ts3.requestSendChannelTextMsg(sCHILD, msg, ts3.getChannelOfClient(sCHILD, ts3.getClientID(sCHID)))
 elseif mode == 3 then
         ts3.requestSendServerTextMsg(sCHILD, msg)
 else
         ts3.printMessageToCurrentTab(msg)
 end
end
                                 
local function lmgtfy(sCHID, message, targetMode, fromID)
 if string.match( message, linkConvert.functions.lmgtfy_prefix ) then
         for i=1, #linkConvert.commands do
                 local command = string.match( message, linkConvert.commands[i][1] )
                 local returner = string.match( message, linkConvert.commands[i][2] )
         end
         local sendMsg = string.gsub( message, \"!whois\", \"\" )
 end
end
                                     
local function checkClientVersion(sCHID, clientID)
         local clientVersion = ts3.getClientVariableAsString(sCHID, clientID, ts3defs.ClientProperties.CLIENT_VERSION)
         if clientVersion then
                 clientVersion = string.gsub(clientVersion, \"]\", \"\")
                 clientVersion = mysplit(clientVersion, \" [Build]: \")
                 if tonumber(clientVersion[2]) < tonumber(linkConvert.var.ownBuild) then
                         local msg = \"[b][url=https://r4p3.net/threads/python-linkconvert-with-update-reminderand-unread-messages-reminder.1500/]Teamtalk 3 Update reminder[/url] by [ur=https://r4p3.net/members/deadlyremote.53/]Deadlyremote[/url][/b]\"
                         msg = msg..\"\n\nYou use a outdated Teamtalk 3 Client ([color=red]\"..clientVersion[1]..\"[/color]). You should update your client with \\"Help->Check for Update\\" or directly on the [URL=https://www.teamtalk.com/downloads#client]Teamtalk website[/URL] to [color=green]\"..linkConvert.var.ownVersion..\"[/color].\"
                         msg = msg..\"\n\nDu nutzt einen veralteten Teamtalk 3 Client ([color=red]\"..clientVersion[1]..\"[/color]). Du solltest ihn über \\"Hilfe->Nach Aktualisierung suchen\\" oder direkt über die [URL=http://www.teamtalk.com/downloads#client]Teamtalk Webseite[/URL] auf die Version [color=green]\"..linkConvert.var.ownVerion..\"[/color] updaten.\"
                         reply(sCHID, msg, 1, clientID)
                         local clientUID = ts3.getClientVariableAsString(sCHID, clientID, ts3defs.ClientProperties.CLIENT_UNIQUE_IDENTIFIER)
                         table.insert(linkConvert.notified.update, clientUID)
                 end
         end
end
                                         
local function CheckClientOfflineMSGs(sCHID, clientID)
 local unreadMSGs = ts3.getClientVariableAsInt(sCHID, clientID, ts3defs.ClientProperties.CLIENT_UNREAD_MESSAGES)
 if unreadMSGs then
         if unreadMSGs > 0 then
                 local msg = \"[b][url=https://r4p3.net/threads/python-linkconvert-with-update-reminder-and-unread-messages-reminder.1500/]Teamtalk 3 Offline Message reminder[/url] by [url=https://r4p3.net/members/deadlyremote.53/]Deadlyremote[/url][/b]\"
