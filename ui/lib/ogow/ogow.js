/* ===================================================
 * Copyright 2013 ZathraC.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 * ========================================================== */
(function ($) {

    $.fn.fbfeed = function (id) {
        var info = "https://graph.facebook.com/" + id + "/"
        var feed = "https://graph.facebook.com/" + id + "/feed?access_token=170597049775092|Z5gUnx7kDEfGqucCJTGXT-L_QYA";
        $("#post").addClass('media ').css({
            'padding-left': '10px'
        });
        $.getJSON(feed, function (fbresults) {
            $("#loading").hide();
            $.each(fbresults.data, function (key, value) {
                if (value.type == 'status') {
                    $("#post").append("<img class='media-object pull-left img-thumbnail' src='http://graph.facebook.com/" + value.from.id + "/picture'>")
                    $("#post").append("<div class='media-body'><h5 class=' media-heading'><a href='http://facebook.com/" + value.from.id + "'>" + value.from.name + "</a></h5><p >" + value.message + "</p></div>")
                    $("#post").append("<hr/>")
                } else if (value.type == 'photo') {
                    var lar_puic = value.picture;
                    lar_puic = lar_puic.replace("_s", "_n");
                    $("#post").append("<img  class='media-object pull-left img-thumbnail' src='http://graph.facebook.com/" + value.from.id + "/picture'>")
                    $("#post").append("<div class='media-body'><h5 class=' media-heading' ><a href='http://facebook.com/" + value.from.id + "'>" + value.from.name + "</a></h5><a href=" + lar_puic + "><img class='pic' src=" + value.picture + "></a><p >" + value.message + "</p></div>")
                    $("#post").append("<hr/>")

                } else if (value.type == 'link') {
                    $("#post").append("<img class='media-object pull-left img-thumbnail' src='http://graph.facebook.com/" + value.from.id + "/picture'>")
                    $("#post").append("<div class='media-body'><h5 class='media-heading'><a href='http://facebook.com/" + value.from.id + "'>" + value.from.name + "</a></h5><p >" + value.message + "</p><p><a  href=" + value.link + ">" + value.name + "</a></p></div>")
                    $("#post").append("<hr/>")
                }
            });
        });
        $.getJSON(info, function (fbresults) {
            $("#post").append("<h3>" + fbresults.name + "</h3>");
        });
    }
    $.fn.members = function (id) {
        var info = "https://graph.facebook.com/" + id + "/";
        
        var members = "https://graph.facebook.com/" + id + "/members?access_token=170597049775092|Z5gUnx7kDEfGqucCJTGXT-L_QYA";
        $.getJSON(members, function (fbresults) {
            $.each(fbresults.data, function (key, value) {

                $("#members").append("<img class='media-object pull-left img-thumbnail' src='http://graph.facebook.com/" + value.id + "/picture'>")
                $("#members").append("<div class='media-body'><h5 class='media-heading'><a href='http://facebook.com/" + value.id + "'>" + value.name + "</a></h5></div>")
                $("#members").append("<hr/>")
            });
        });
    }
}(jQuery));