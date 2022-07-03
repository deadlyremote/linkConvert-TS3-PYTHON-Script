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
