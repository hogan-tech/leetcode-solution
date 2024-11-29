<h2><a href="https://leetcode.com/problems/event-emitter/">2694. Event Emitter</a></h2><h3>Medium</h3><hr><div><p>Design an <code>EventEmitter</code> class. This interface&nbsp;is similar (but with some differences) to the one found in Node.js or the Event Target interface of the DOM. The <code>EventEmitter</code> should allow for subscribing to events and emitting them.</p>

<p>Your <code>EventEmitter</code> class should have the following two methods:</p>

<ul>
	<li><strong>subscribe</strong> - This method takes in two arguments: the name of an event as a string and a callback function. This callback function&nbsp;will later be called when the event is emitted.<br>
	An event should be able to have multiple listeners for the same event. When emitting an event with multiple callbacks, each should be called in the order in which they were subscribed. An array of results should be returned. You can assume no callbacks passed to&nbsp;<code>subscribe</code>&nbsp;are referentially identical.<br>
	The <code>subscribe</code> method should also return an object with an <code>unsubscribe</code>&nbsp;method that enables the user to unsubscribe. When it is called, the callback&nbsp;should be removed from the list of subscriptions and&nbsp;<code>undefined</code>&nbsp;should be returned.</li>
	<li><strong>emit</strong> - This method takes in two arguments: the name of an event as a string and an optional array of arguments that will be&nbsp;passed to the callback(s). If there are no callbacks subscribed to the given event, return an empty array. Otherwise, return an array of the results of all callback calls in the order they were subscribed.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> actions = ["EventEmitter", "emit", "subscribe", "subscribe", "emit"], values = [[], ["firstEvent", "function cb1() { return 5; }"],  ["firstEvent", "function cb1() { return 5; }"], ["firstEvent"]]
<strong>Output:</strong> [[],["emitted",[]],["subscribed"],["subscribed"],["emitted",[5,6]]]
<strong>Explanation:</strong> 
const emitter = new EventEmitter();
emitter.emit("firstEvent"); // [], no callback are subscribed yet
emitter.subscribe("firstEvent", function cb1() { return 5; });
emitter.subscribe("firstEvent", function cb2() { return 6; });
emitter.emit("firstEvent"); // [5, 6], returns the output of cb1 and cb2
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> actions = ["EventEmitter", "subscribe", "emit", "emit"], values = [[], ["firstEvent", "function cb1(...args) { return args.join(','); }"], ["firstEvent", [1,2,3]], ["firstEvent", [3,4,6]]]
<strong>Output:</strong> [[],["subscribed"],["emitted",["1,2,3"]],["emitted",["3,4,6"]]]
<strong>Explanation: </strong>Note that the emit method should be able to accept an OPTIONAL array of arguments.

const emitter = new EventEmitter();
emitter.subscribe("firstEvent, function cb1(...args) { return args.join(','); });
emitter.emit("firstEvent", [1, 2, 3]); // ["1,2,3"]
emitter.emit("firstEvent", [3, 4, 6]); // ["3,4,6"]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> actions = ["EventEmitter", "subscribe", "emit", "unsubscribe", "emit"], values = [[], ["firstEvent", "(...args) =&gt; args.join(',')"], ["firstEvent", [1,2,3]], [0], ["firstEvent", [4,5,6]]]
<strong>Output:</strong> [[],["subscribed"],["emitted",["1,2,3"]],["unsubscribed",0],["emitted",[]]]
<strong>Explanation:</strong>
const emitter = new EventEmitter();
const sub = emitter.subscribe("firstEvent", (...args) =&gt; args.join(','));
emitter.emit("firstEvent", [1, 2, 3]); // ["1,2,3"]
sub.unsubscribe(); // undefined
emitter.emit("firstEvent", [4, 5, 6]); // [], there are no subscriptions
</pre>

<p><strong class="example">Example 4:</strong></p>

<pre><strong>Input:</strong> actions = ["EventEmitter", "subscribe", "subscribe", "unsubscribe", "emit"], values = [[], ["firstEvent", "x =&gt; x + 1"], ["firstEvent", "x =&gt; x + 2"], [0], ["firstEvent", [5]]]
<strong>Output:</strong> [[],["subscribed"],["emitted",["1,2,3"]],["unsubscribed",0],["emitted",[7]]]
<strong>Explanation:</strong>
const emitter = new EventEmitter();
const sub1 = emitter.subscribe("firstEvent", x =&gt; x + 1);
const sub2 = emitter.subscribe("firstEvent", x =&gt; x + 2);
sub1.unsubscribe(); // undefined
emitter.emit("firstEvent", [5]); // [7]</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= actions.length &lt;= 10</code></li>
	<li><code>values.length === actions.length</code></li>
	<li>All test cases are valid, e.g. you don't need to handle scenarios when unsubscribing from a non-existing subscription.</li>
	<li>There are only 4 different actions: <code>EventEmitter</code>, <code>emit</code>, <code>subscribe</code>, and <code>unsubscribe</code>.</li>
	<li>The <code>EventEmitter</code> action doesn't take any arguments.</li>
	<li>The <code>emit</code>&nbsp;action takes between either 1 or&nbsp;2&nbsp;arguments. The first argument is the name of the event we want to emit, and the 2nd argument is passed to the callback functions.</li>
	<li>The <code>subscribe</code> action takes 2 arguments, where the first one is the event name and the second is the callback function.</li>
	<li>The <code>unsubscribe</code>&nbsp;action takes one argument, which is the 0-indexed order of the subscription made before.</li>
</ul>
</div>